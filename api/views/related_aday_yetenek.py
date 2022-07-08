from rest_framework import viewsets, filters
from api.models import RelatedAdayYetenek
from api.serializers.related_aday_yetenek import RelatedAdayYetenekSerializers
from django_filters.rest_framework import DjangoFilterBackend


class RelatedAdayYetenekViewSet(viewsets.ModelViewSet):
    queryset = RelatedAdayYetenek.objects.all()
    serializer_class = RelatedAdayYetenekSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('aday', 'yetenek')


