from django.core.files.storage import FileSystemStorage
from django.db import models
import uuid
from users.models import Profiles
from django.utils.text import slugify


class Project(models.Model):
    owner = models.ForeignKey(Profiles, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def custom_upload_folder(self):
        return self.slug


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
