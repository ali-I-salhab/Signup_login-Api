from rest_framework import serializers 
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[         'username',
            'first_name',
            'last_name',
            'email',
            'password',]
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]