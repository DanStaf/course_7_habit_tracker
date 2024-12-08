from django.core.management import BaseCommand
from users.tasks import send_reminder_to_users


class Command(BaseCommand):

    def handle(self, *args, **options):

        print("Task started for testing")

        send_reminder_to_users()

        print("Task finished")
