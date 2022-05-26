from ast import mod
from django.db import models
import uuid


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    name = models.CharField(max_length=255, null=True, blank=True)
    shares = models.IntegerField(default=0)
    reaction_count = models.IntegerField(default=0)
    comments = models.IntegerField(default=0, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    posted_on = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.CharField(max_length=255, null=True, blank=True)
    video = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    post_url = models.URLField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    loves = models.IntegerField(default=0)
    wow = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    haha = models.IntegerField(default=0)
    cares = models.IntegerField(default=0)
    post_id = models.IntegerField(default=0)
    page_id = models.IntegerField(default=0)
    cursor = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name + "--" + str(self.posted_on)

    class Meta():
        ordering = ['posted_on']
