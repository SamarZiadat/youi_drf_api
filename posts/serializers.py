from rest_framework import serializers
from posts.models import Post
from taggit.serializers import TagListSerializerField, TaggitSerializer
from likes.models import Like


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Serializer for the Post model
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    tags = TagListSerializerField()
    profile_image = serializers.ReadOnlyField(
        source="owner.profile.profile_picture.url"
    )

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

    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "content",
            "tags",
            "image",
        ]
