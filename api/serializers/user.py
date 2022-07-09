from rest_framework import serializers
from api.models import User


class UserSerializersForGet(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'foto', 'durum')

