import datetime

from django.core.management.base import BaseCommand
from seminar_app2.models import Autor


class Command(BaseCommand):
    help = 'Creates new users'

    def handle(self, *args, **options):
        for i in range(1, 11):
            author = Autor(name=f'Author{i}', last_name=f'Last name{i}', email=f'email{i}@mail.ru',
                           bio=f'bio{i}', birthday=datetime.date(2000,1, 1))
            self.stdout.write(self.style.ERROR(f'Author{author} created'))
            author.save()
