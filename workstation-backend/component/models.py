from django.db import models
from workspace import models as workspace_models

# Create your models here.
class BaseComponent(models.Model):
    workspace_id = models.ForeignKey(
        workspace_models.Workspace, on_delete=models.CASCADE
    )
    x = models.DecimalField(max_digits=100, decimal_places=2)
    y = models.DecimalField(max_digits=100, decimal_places=2)
    width = models.DecimalField(max_digits=100, decimal_places=2)
    height = models.DecimalField(max_digits=100, decimal_places=2)
    collapsed = models.BooleanField(default=False)

    class Meta:
        abstract = True


# Checklist component
class Checklist(BaseComponent):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=10, default="#baaf13")


class ChecklistItem(models.Model):
    checklist_id = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_checked = models.BooleanField()


class PostIt(BaseComponent):
    content = models.TextField()
    color = models.CharField(max_length=10, default="#baaf13")


class Image(BaseComponent):
    url = models.URLField()
