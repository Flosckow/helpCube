from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

from blogs.managers import PostActiveManager


class Post(models.Model):
    """Статьи пользователя"""

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to="blog-images")
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
