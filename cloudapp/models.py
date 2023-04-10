from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    return '{1}'.format(instance.id, filename)


class Post(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.name
    
    @property
    def file_url(self):
        return f"https://qazcloud1.s3.eu-central-1.amazonaws.com/media/{self.file}"