from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                **{'first_name': 'Super',
                   'last_name': 'User',
                   'email': 'super@user.help',
                   'password': '***supeRUser***',
                   'is_active': True,
                   'is_superuser': True,
                   'is_staff': True
                   }
            )
        except Exception as e:
            print(str(e))
