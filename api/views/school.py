from rest_framework import viewsets, filters
from api.models import School
from api.serializers.school import SchoolSerializers


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializers


