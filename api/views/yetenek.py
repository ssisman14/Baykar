from rest_framework import viewsets, filters
from api.models import Yetenekler
from api.serializers.yetenek import YetenekSerializers


class YetenekViewSet(viewsets.ModelViewSet):
    queryset = Yetenekler.objects.all()
    serializer_class = YetenekSerializers


