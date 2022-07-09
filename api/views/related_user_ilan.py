from rest_framework import viewsets, filters
from api.models import RelatedIlanKullanici
from api.serializers.related_user_ilan import RelatedUserIlanSerializers, RelatedUserIlanForGetSerializers
from django_filters.rest_framework import DjangoFilterBackend


class RelatedUserIlanViewSet(viewsets.ModelViewSet):
    queryset = RelatedIlanKullanici.objects.all()
    serializer_class = RelatedUserIlanSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('user', 'ilan')

    def get_serializer_class(self):
        if self.request:
            if self.request.method != 'GET':
                return RelatedUserIlanSerializers
        return RelatedUserIlanForGetSerializers
