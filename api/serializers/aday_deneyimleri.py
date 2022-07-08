from rest_framework import serializers
from api.models import AdayDeneyimler
from api.serializers import CompanySerializers


class AdayDeneyimleriSerializers(serializers.ModelSerializer):

    class Meta:
        model = AdayDeneyimler
        fields = '__all__'


class AdayDeneyimleriForGetSerializers(serializers.ModelSerializer):
    company = CompanySerializers(read_only=True)

    class Meta:
        model = AdayDeneyimler
        fields = '__all__'