from api.views import FavoriteView
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('favorites', FavoriteView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
]