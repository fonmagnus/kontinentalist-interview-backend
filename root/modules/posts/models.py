from django.db import models
from accounts.models import UserAccount

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
