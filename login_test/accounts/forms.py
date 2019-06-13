# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import User

#-- User form
class UserForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserForm, self).__init__(*args, **kwargs)
                                       
    def clean_email(self):
        #raise forms.ValidationError('error pichurriento')
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email, is_active=True):
            raise forms.ValidationError('Este correo ya ha sido registrado')
        print('mail: ',email)
        return email

    first_name = forms.CharField(
        label = 'Nombre',
        #error_messages = {'required':'cmapo no valido'},
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label = 'Apellidos', 
        #error_messages = {'required':'Enter a valid phone number'},
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        label = 'Correo',
        #error_messages = {'required':'Este campo es requerido', 'invalid':'correo mal'},
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    phone = forms.CharField(
        label = 'Teléfono', 
        #error_messages = {'required':'Enter a valid phone number'},
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id' : 'mask_phone'
            }
        )
    )
        
    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'phone',  )


