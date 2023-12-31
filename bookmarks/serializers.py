from django.db import IntegrityError
from rest_framework import serializers
from bookmarks.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    """
    Serializer for the Bookmark model
    The create method handles the unique constraint on 'owner' and 'event'
    """

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Bookmark
        fields = ["id", "created_at", "owner", "event"]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
