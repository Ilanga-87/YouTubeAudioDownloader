from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class Conversion(models.Model):
    video_id = models.CharField("ID video", default="", max_length=100)
    video_url = models.CharField('URL to Youtube', max_length=255)
    title = models.CharField('Video title', max_length=100, blank=True)
    audio_url = models.CharField('URL to created audio', max_length=255, blank=True)
    pub_time = models.TimeField('Publish time', blank=True, null=True)
    slug = models.SlugField(default=" ", max_length=255, blank=True, null=False)
    audio_file = models.FileField(upload_to="audio", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('audio-page', args=self.slug)
