from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User.objects.create(
            email='danstaf@mail.ru',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()

        user = User.objects.create(
            email='danstaf1@mail.ru',
            first_name='Sender',
            last_name='Sender',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('12345')
        user.save()

        user = User.objects.create(
            email='danstaf2@mail.ru',
            first_name='Manager',
            last_name='Manager',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('12345')
        user.save()

        print("Users created")
