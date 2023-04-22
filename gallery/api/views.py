from api.serializers import FavoriteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from photo.models.favorites import Favorite


class FavoriteView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

