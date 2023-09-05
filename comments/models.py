from django.db import models
from django.utils import timezone
from users.models import SiteUser


class Comment(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    post = models.TextField(max_length=250)
    date = models.DateTimeField(default=timezone.now)
    page = models.SlugField()
