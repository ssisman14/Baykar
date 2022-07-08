from rest_framework import serializers
from api.models import User
from django.core import exceptions
import django.contrib.auth.password_validation as validators


class UserSerializersForGet(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'foto', 'durum')

