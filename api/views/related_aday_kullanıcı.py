from rest_framework import viewsets, filters
from api.models import RelatedAdayKullanici
from api.serializers.related_aday_kullanıcı import RelatedAdayKullaniciSerializers, RelatedAdayKullaniciForGetSerializers
from django_filters.rest_framework import DjangoFilterBackend


class RelatedAdayKullaniciViewSet(viewsets.ModelViewSet):
    queryset = RelatedAdayKullanici.objects.all()
    serializer_class = RelatedAdayKullaniciSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('aday', 'user')

    def get_serializer_class(self):
        if self.request:
            if self.request.method != 'GET':
                return RelatedAdayKullaniciSerializers
        return RelatedAdayKullaniciForGetSerializers