from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "location",
            "portfolio_url",
            "job_title",
            "current_employer",
            "about",
            "work_experience",
            "certifications",
            "education",
            "profile_picture",
        ]
