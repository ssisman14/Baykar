from rest_framework import viewsets, filters
from api.models import RelatedCompanyUser
from api.serializers.related_company_user import RelatedCompanyUserSerializers
from django_filters.rest_framework import DjangoFilterBackend


class RelatedCompanyUserViewSet(viewsets.ModelViewSet):
    queryset = RelatedCompanyUser.objects.all()
    serializer_class = RelatedCompanyUserSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('company', 'user')


