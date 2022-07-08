from rest_framework import viewsets, filters
from api.models import Company
from api.serializers.company import CompanySerializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


