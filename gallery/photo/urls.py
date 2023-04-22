from django.urls import path

from photo.views.index import IndexView

from photo.views.photo import PhotoCreateView, PhotoUpdateView, PhotoDetailView, PhotoDeleteView

from photo.views.favorites import FavoriteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<int:pk>/to-favorite', FavoriteView.as_view(), name='to_favorite'),
]
