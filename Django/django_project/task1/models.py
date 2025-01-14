from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



#python manage.py makemigrations
#python manage.py migrate


"""
            Список QuerySet запросов в порядке вызовов 

python manage.py shell 

from task1.models import Buyer, Game

        Открытие в Buyer объектов Ilia, Terminator2000, Ubivator432 

Buyer.objects.create(name='Ilia', balance=1500.05, age=24)
Buyer.objects.create(name='Terminator2000', balance=42.15, age=52)
Buyer.objects.create(name='Ubivator432', balance=0.5 ,age=16) 

        Открытие в Game объектов Cyberpunk2077, Mario, Hitman 

Game.objects.create(title='Cyberpunk2077', cost=31, size=46.2, description='Game of the year', age_limited=True)
Game.objects.create(title='Mario', cost=5, size=0.5, description='Old game', age_limited=False)  
Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=True) 

        Сохранение покупателей в переменных

b1 = Buyer.objects.get(id=1)
b2 = Buyer.objects.get(id=2)
b3 = Buyer.objects.get(id=3)

        Сохранение игр в переменных 

g1 = Game.objects.get(id=1)      
g2 = Game.objects.get(id=2)
g3 = Game.objects.get(id=3)      

        Связывание объектов с полем buyer у записей Game

g1.buyer.set([b1, b2])  - Первой игрой владеют Ilia(b1) и Terminator2000(b2)
g2.buyer.set([b1, b3])  - Второй игрой владеют Ilia(b1) и Terminator2000(b2) и Ubivator432(b3)
g3.buyer.set([b1, b2])  - Третьей игрой владеет Ilia(b1)

"""


