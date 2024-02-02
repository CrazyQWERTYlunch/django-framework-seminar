from django.db import models


class Coin(models.Model):
    side = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.side}: {self.time_created}'

    @staticmethod
    def get_data(count):
        coints = Coin.objects.all()[:count]
        coints_dict = {
            'heads': [],
            'tales': [],
        }
        for coin in coints:
            if coin.side == 0:
                coints_dict['heads'].append(coin.time_created)
            else:
                coints_dict['tales'].append(coin.time_created)
        return coints_dict


class Autor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def __str__(self):
        return f'Author: {self.name} {self.last_name}, birthday: {self.birthday}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}'
