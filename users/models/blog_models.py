from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

from users.managers import PostActiveManager


class Post(models.Model):
    """Статьи пользователя"""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    text = RichTextUploadingField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostActiveManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
