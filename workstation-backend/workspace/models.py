from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Workspace(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Background(models.Model):
    workspace_id = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    image_url = models.URLField()
