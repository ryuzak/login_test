from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	date_joined = serializers.ReadOnlyField()

	class Meta(object):
		model = User
		fields = ('id','email', 'first_name', 'last_name', 'date_joined', 'password', 'is_active')
		extra_kwargs = {'password':{'write_only':True}}

	def create(self, validated_data):
		user = User(
			email = validated_data['email'],
			first_name = validated_data['first_name'],
			last_name = validated_data['last_name'],
			is_active = True
		)
		print(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user