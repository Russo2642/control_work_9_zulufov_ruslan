from django.views.generic import TemplateView, ListView

from photo.models import Photo


class IndexView(ListView):
    template_name = 'index.html'
    model = Photo
    ordering = ['-created_at']
    context_object_name = 'photos'
