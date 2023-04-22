from rest_framework import serializers

from photo.models.favorites import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'photo')
        read_only_fields = ('id',)
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        request = self.context.get('request')
        favorite = Favorite()
        favorite.photo = validated_data['photo']
        favorite.user = request.user
        favorite.save()
        return favorite
