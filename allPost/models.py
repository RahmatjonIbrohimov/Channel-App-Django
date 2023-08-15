from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class post(models.Model):
    # post_img = models.ImageField()
    post_auth = models.ForeignKey(User, on_delete=models.CASCADE)
    post_header = models.CharField(max_length=50)
    post_content = models.CharField(max_length=255)
    post_date = models.DateTimeField(default=timezone.datetime.now)

    def __str__(self):
        return f'by: {self.post_auth}   -|-   {self.post_header}'
