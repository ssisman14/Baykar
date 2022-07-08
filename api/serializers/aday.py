from rest_framework import serializers
from api.models import AdayBilgileri


class AdaySerializers(serializers.ModelSerializer):
    class Meta:
        model = AdayBilgileri
        fields = '__all__'