from rest_framework import viewsets, filters
from api.models import User
from api.serializers.user import  UserSerializersForGet
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializersForGet
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filterset_fields = ('username', 'email', 'id')


