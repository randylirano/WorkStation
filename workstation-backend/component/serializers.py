from rest_framework import serializers

from .models import PostIt
from workspace.models import Workspace


class BaseComponentSerializer(serializers.ModelSerializer):
    workspace_id = serializers.UUIDField()

    def create(self, validated_data):
        workspace_id = validated_data.get("workspace_id")

        # Check that the workspace exists.
        # TODO: when we add authentication, check that the workspace belongs to the user
        if workspace_id is None or not Workspace.objects.filter(id=workspace_id).exists():
            raise serializers.ValidationError(
                {"workspace_id": "Workspace doesn't exist"}
            )

        return super().create(validated_data)

    class Meta:
        abstract = True
        fields = [
            "id",
            "workspace_id",
            "x",
            "y",
            "width",
            "height",
        ]
        read_only_fields = ["workspace_id"]


class PostItSerializer(BaseComponentSerializer):
    class Meta:
        model = PostIt
        fields = BaseComponentSerializer.Meta.fields + ["title", "content", "color", "collapsed"]
