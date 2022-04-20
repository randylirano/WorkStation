from uuid import uuid4

from django.db import models
from workspace import models as workspace_models

# Create your models here.
# Reusable abstract base model.
class BaseComponent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    workspace = models.ForeignKey(workspace_models.Workspace, on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=100, decimal_places=2)
    y = models.DecimalField(max_digits=100, decimal_places=2)
    width = models.DecimalField(max_digits=100, decimal_places=2)
    height = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        abstract = True


# Checklist model
class Checklist(BaseComponent):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=10, default="#baaf13")
    collapsed = models.BooleanField(default=False)


# Checklist item model
class ChecklistItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    checklist_id = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_checked = models.BooleanField()
    ordering = models.IntegerField(default=0)


# Post-it model
class PostIt(BaseComponent):
    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(max_length=10, default="#baaf13")
    collapsed = models.BooleanField(default=False)


# Image model
class Image(BaseComponent):
    url = models.URLField()
