from rest_framework import serializers
from api.models import Ilan, RelatedIlanKullanici
from api.serializers.company import CompanySerializers


class IlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ilan
        fields = '__all__'


class IlanForGetSerializers(serializers.ModelSerializer):
    company = CompanySerializers(read_only=True)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Ilan
        fields = '__all__'

    @staticmethod
    def count(obj):
        return RelatedIlanKullanici.objects.filter(ilan=obj.id).count()