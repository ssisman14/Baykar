from rest_framework import serializers
from api.models import Yetenekler


class YetenekSerializers(serializers.ModelSerializer):
    class Meta:
        model = Yetenekler
        fields = '__all__'