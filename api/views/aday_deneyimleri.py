from rest_framework import viewsets, filters
from api.models import AdayDeneyimler
from api.serializers.aday_deneyimleri import AdayDeneyimleriSerializers, AdayDeneyimleriForGetSerializers
from django_filters.rest_framework import DjangoFilterBackend


class AdayDeneyimleriViewSet(viewsets.ModelViewSet):
    queryset = AdayDeneyimler.objects.all()
    serializer_class = AdayDeneyimleriSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('sirket', 'user')

    def get_serializer_class(self):
        if self.request:
            if self.request.method != 'GET':
                return AdayDeneyimleriSerializers
        return AdayDeneyimleriForGetSerializers