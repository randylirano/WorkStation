from rest_framework import serializers

from .models import PostIt, Checklist, ChecklistItem, Image
from workspace.models import Workspace


# Serializer for abstract base model
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


# Post-it serializer
class PostItSerializer(BaseComponentSerializer):
    class Meta:
        model = PostIt
        fields = BaseComponentSerializer.Meta.fields + ["title", "content", "color", "collapsed"]


# Checklist serializer
class ChecklistSerializer(BaseComponentSerializer):
    class Meta:
        model = Checklist
        fields = BaseComponentSerializer.Meta.fields + ["title", "color", "collapsed"]


# Checklist item serializer
class ChecklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = ["id", "content", "checked", "ordering"]
        read_only_fields = ["checklist_id"]


# Image serializer
class ImageSerializer(BaseComponentSerializer):
    class Meta:
        model = Image
        fields = BaseComponentSerializer.Meta.fields + ["url"]
