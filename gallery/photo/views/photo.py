from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from photo.forms import PhotoForm
from photo.models import Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo/photo_create.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class PhotoDetailView(DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo


class PhotoUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'photo/photo_update.html'
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('photo.change_photo')


class PhotoDeleteView(UserPassesTestMixin, DeleteView):
    model = Photo

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.author_id})

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('photo.delete_photo')
