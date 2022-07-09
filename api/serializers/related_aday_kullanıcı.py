from rest_framework import serializers
from api.models import RelatedAdayKullanici
from api.serializers.school import SchoolSerializers


class RelatedAdayKullaniciSerializers(serializers.ModelSerializer):

    class Meta:
        model = RelatedAdayKullanici
        fields = '__all__'


class RelatedAdayKullaniciForGetSerializers(serializers.ModelSerializer):
    school = SchoolSerializers(read_only=True)

    class Meta:
        model = RelatedAdayKullanici
        fields = '__all__'