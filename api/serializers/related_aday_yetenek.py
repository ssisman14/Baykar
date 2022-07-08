from rest_framework import serializers
from api.models import RelatedAdayYetenek


class RelatedAdayYetenekSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelatedAdayYetenek
        fields = '__all__'