from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("E-mail"), max_length=60, unique=True)

    first_name = models.CharField(_("First name"), max_length=70)
    last_name = models.CharField(_("Last name"), max_length=70)

    avatar = models.ImageField(_("Avatar"), upload_to="users/avatars", blank=True, null=True)

    # dates
    date_joined = models.DateTimeField(_("Creation date"), auto_now_add=True)
    last_login = models.DateTimeField(_("Last visited"), auto_now=True)

    # extra fields
    is_active = models.BooleanField(_("Active"), default=False)
    is_superuser = models.BooleanField(_("Superuser"), default=False)
    is_staff = models.BooleanField(_("Access to admin"), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name',)

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}[0]"
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Sending email to user """
        send_mail(subject, message, from_email, [self.email], **kwargs)
