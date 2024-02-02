from django.core.management.base import BaseCommand
from seminar_app2.models import Autor

class Command(BaseCommand):
    help = 'Deletes an author by id'

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Counts new clients')

    def handle(self, *args, **kwargs):
        pk = kwargs['id']

        author = Autor.objects.filter(pk=pk).first()

        author.delete()
        self.stdout.write(self.style.ERROR(f'Deleted author {author}'))
