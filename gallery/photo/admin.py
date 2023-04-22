from django.contrib import admin

from photo.models.photo import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'signature', 'author', 'created_at', 'updated_at')


admin.site.register(Photo, PhotoAdmin)
