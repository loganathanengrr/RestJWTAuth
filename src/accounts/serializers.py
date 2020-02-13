from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import exceptions as django_exceptions
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User =  get_user_model()

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(
		style={'input_type': 'password'},min_length=6, max_length=100,
		write_only=True
		)
	password2 = serializers.CharField(
		style={'input_type': 'password'},min_length=6,max_length=100,
		write_only=True
		)

	class Meta:
		model = User
		fields = (
			User._meta.pk.name,
			User.USERNAME_FIELD,
			) + tuple(User.REQUIRED_FIELDS) + ('password','password2')

	def validate(self, attrs):
		# Make user instance
		attrs = super(UserSerializer, self).validate(attrs) 
		user = self.instance

		password = attrs.get('password')
		password2 = attrs.get('password2')
		match = password == password2
		print(dir(self))
		
		if(match):
			try:
				#validate the passwords againts password validators
				validate_password(password, user) 
			except django_exceptions.ValidationError as e:
				raise serializers.ValidationError(list(e.messages))
		
		else:
			raise serializers.ValidationError("Password mismatch, Please enter passwords carefully.")
		
		return attrs
	
	def create(self, validated_data):
		user = self.Meta.model.objects.create_user(
			email = validated_data.get('email'),
			date_of_birth = validated_data.get('date_of_birth'),
			password = validated_data.get('password')
		)

		return user
		





