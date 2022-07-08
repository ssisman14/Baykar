from rest_framework import serializers
from api.models import RelatedCompanyUser


class RelatedCompanyUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelatedCompanyUser
        fields = '__all__'