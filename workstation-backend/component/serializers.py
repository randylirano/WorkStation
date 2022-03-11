from rest_framework import serializers

from .models import PostIt
from workspace.models import Workspace


class BaseComponentSerializer(serializers.ModelSerializer):
    workspace_id = serializers.UUIDField(
        source="workspace.id",
        read_only=True,
    )

    def create(self, validated_data):
        workspace_id = self.context["view"].kwargs.get("workspace_id")

        if workspace_id is None:
            raise serializers.ValidationError({"workspace_id": "Must not be null."})

        # Check that the workspace exists.
        # TODO: when we add authentication, check that the workspace belongs to the user
        if not Workspace.objects.filter(id=workspace_id).exists():
            raise serializers.ValidationError(
                {"workspace_id": "Workspace doesn't exist"}
            )

        validated_data["workspace_id"] = workspace_id
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
