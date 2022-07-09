from rest_framework import viewsets, filters
from api.models import Ilan
from api.serializers.ilan import IlanSerializers, IlanForGetSerializers
from django_filters.rest_framework import DjangoFilterBackend


class IlanViewSet(viewsets.ModelViewSet):
    queryset = Ilan.objects.all()
    serializer_class = IlanSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('yayinlayan', 'company', 'id', 'type', 'city')

    def get_serializer_class(self):
        if self.request:
            if self.request.method != 'GET':
                return IlanSerializers
        return IlanForGetSerializers