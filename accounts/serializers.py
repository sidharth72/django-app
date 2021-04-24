from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegister(serializers.ModelSerializer):

	password2 = serializers.CharField(max_length=100,style={'input_type':'password'})

	class Meta:
		model = User
		fields=['first_name','username','password','password2']

	def save(self):

		reg = User(
			email=self.validated_data['email'],
			username = self.validated_data['username']


		)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']

		if password != password2:
			raise serializers.ValidationError({"password":"password dosen't match!"})

		reg.set_password(password)
		reg.save()

		return reg





