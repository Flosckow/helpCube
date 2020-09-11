from django.db import models


class PostActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)