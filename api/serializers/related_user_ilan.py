from rest_framework import serializers
from api.models import RelatedIlanKullanici
from .user import UserSerializersForGet
from .ilan import IlanForGetSerializers


class RelatedUserIlanSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelatedIlanKullanici
        fields = '__all__'


class RelatedUserIlanForGetSerializers(serializers.ModelSerializer):
    user = UserSerializersForGet(read_only=True)
    ilan = IlanForGetSerializers(read_only=True)

    class Meta:
        model = RelatedIlanKullanici
        fields = '__all__'