from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspace(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Background(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    workspace = models.OneToOneField(Workspace, on_delete=models.CASCADE)
    image_url = models.TextField()
