from rest_framework import viewsets
from api.models import AdayBilgileri
from api.serializers.aday import AdaySerializers


class AdayViewSet(viewsets.ModelViewSet):
    queryset = AdayBilgileri.objects.all()
    serializer_class = AdaySerializers