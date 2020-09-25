from django.db import models


class TokenUser(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.DO_NOTHING)
    token = models.CharField(
        max_length=180,
    )
    expiration_date = models.DateTimeField()

    class Meta:
        ordering = [
            "-expiration_date",
        ]
