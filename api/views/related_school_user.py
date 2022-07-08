from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser
from api.models import RelatedUserSchool
from api.serializers.related_school_user import RelatedUserSchoolSerializers, RelatedUserSchoolForGetSerializers
from django_filters.rest_framework import DjangoFilterBackend


class RelatedUserSchoolViewSet(viewsets.ModelViewSet):
    queryset = RelatedUserSchool.objects.all()
    serializer_class = RelatedUserSchoolSerializers
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('user', 'school')

    def get_serializer_class(self):
        if self.request:
            if self.request.method != 'GET':
                return RelatedUserSchoolSerializers
        return RelatedUserSchoolForGetSerializers