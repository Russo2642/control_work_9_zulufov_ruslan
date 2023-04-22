import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from photo.models import Photo

from photo.models.favorites import Favorite


class FavoriteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        if not Favorite.objects.filter(user=request.user, photo=photo).exists():
            Favorite.objects.create(user=request.user, photo=photo)
        else:
            Favorite.objects.filter(user=request.user, photo=photo).delete()
        return redirect('index')
