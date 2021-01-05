#from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'is_student', 'is_teacher')
        extra_kwargs = {
            'password':{'write_only':True}
        }


class RegistrationSerializer(serializers.ModelSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'is_student', 'is_teacher']
        extra_kwargs = {
            'password': {'write_only':True}
        }

        def save(self):
            user = User(
                email=self.validated_data['email'],
                username=self.validated_data['username'],
            )
            password = self.validated_data['password']
            password2 = self.validated_data['password2']

            if password != password2:
                raise serializers.ValidationError(
                    {'password': 'Password must match!'})
            user.set_password(password)
            user.save()
            return User
