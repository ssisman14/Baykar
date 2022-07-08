from rest_framework import serializers
from api.models import RelatedUserSchool
from api.serializers.school import SchoolSerializers


class RelatedUserSchoolSerializers(serializers.ModelSerializer):

    class Meta:
        model = RelatedUserSchool
        fields = '__all__'


class RelatedUserSchoolForGetSerializers(serializers.ModelSerializer):
    school = SchoolSerializers(read_only=True)

    class Meta:
        model = RelatedUserSchool
        fields = '__all__'