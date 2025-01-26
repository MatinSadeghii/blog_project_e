from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):

    class PublishManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(staus=Post.Staus.PUBLISHED)

    class Staus(models.TextField):
        PUBLISHED = 'PB','Publish'
        DRAFT = 'DR','Draft'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    staus = models.CharField(choices=Staus.choices,max_length=2,default=Staus.DRAFT)

    objects = models.Manager()
    published = PublishManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title