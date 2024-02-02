from django.core.management.base import BaseCommand
from seminar_app2.models import Autor, Post

class Command(BaseCommand):
    help = 'Creates post fill db'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of post to create per author')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        authors = Autor.objects.all()

        for author in authors:
            for i in range(count):
                post = Post(
                    title=f'Title{i}',
                    content=f'Content{i}',
                    author=author
                )
                self.stdout.write(self.style.SUCCESS(f'Createt post {post}'))
                post.save()
