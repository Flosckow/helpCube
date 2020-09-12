from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            call_command('create_superuser')
        except Exception as e:
            print("Error!", str(e))
