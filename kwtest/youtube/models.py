from django.db import models
import uuid


class VietNamTrendVideo(models.Model):
    pos = models.IntegerField(default=0)
    vid_name = models.CharField(max_length=255, null=True, blank=True)
    vid_link = models.URLField(max_length=255, null=True, blank=True)
    embed_link = models.CharField(max_length=255, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vid_name

    class Meta():
        ordering = ['created']


class VietNamMusicVideo(models.Model):
    pos = models.IntegerField(default=0)
    vid_name = models.CharField(max_length=255, null=True, blank=True)
    vid_link = models.URLField(max_length=255, null=True, blank=True)
    embed_link = models.CharField(max_length=255, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vid_name

    class Meta():
        ordering = ['created']
