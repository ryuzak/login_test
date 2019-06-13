# -*- coding: utf-8 -*-
from django.conf import settings
#from django.contrib.auth.hashers import check_password
from accounts.models import User
#from django.contrib.auth import get_user_model
#User = get_user_model()


class EmailAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        print("entro al authenticate")
        try:
            user = User.objects.get(email=email)
            print(user.check_password(password))
            if user.check_password(password):
                return user
        except User.DoesNotExist as ex:
            print(ex)
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
