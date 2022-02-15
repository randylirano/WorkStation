from rest_framework import serializers

from .models import Background


class BackgroundSerializer(serializers.ModelSerializer):
    workspace_id = serializers.IntegerField()
    image_url = serializers.URLField()

    def update(self, instance, validated_data):
        # Remove `workspace_id` from being updated.
        validated_data.pop("workspace_id", None)

        return super().update(instance, validated_data)

    class Meta:
        model = Background
        fields = ["id", "workspace_id", "image_url"]
