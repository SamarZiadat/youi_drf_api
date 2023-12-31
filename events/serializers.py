from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from django.utils.dateformat import format
from bookmarks.models import Bookmark
from .models import Event


class EventSerializer(TaggitSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    tags = TagListSerializerField()
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.profile_picture.url"
    )
    bookmark_id = serializers.SerializerMethodField()
    bookmarks_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size larger than 2MB!")
        if value.image.height > 4096:
            raise serializers.ValidationError("Image height larger than 4096px!")
        if value.image.width > 4096:
            raise serializers.ValidationError("Image width larger than 4096px!")
        return value

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_bookmark_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(owner=user, event=obj).first()
            return bookmark.id if bookmark else None
        return None

    class Meta:
        model = Event
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "description",
            "event_date",
            "tags",
            "category",
            "format",
            "image",
            "bookmark_id",
            "bookmarks_count",
            "reviews_count",
        ]
