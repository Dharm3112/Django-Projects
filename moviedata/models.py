from random import choices
from tkinter.constants import CASCADE

from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name



class maleactor(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name



class femaleactor(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name


class movie(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    actor = models.ForeignKey(maleactor,on_delete=models.CASCADE)
    actress = models.ForeignKey(femaleactor,on_delete=models.CASCADE)
    moviecategory = models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

city_list = [
    ('1','Ahmedabad'),
    ('2','Surat'),
    ('3','Vadodra'),
    ('4','Rajkot'),
    ('5','Morbi'),
    ('6','Anand'),
    ('7','Valsad'),
]


state_list = [
    ('1','Gujarat'),
    ('2','Maharastra'),
    ('3','Goa'),
    ('4','Rajeshthan'),
    ('5','TamilNadu'),
]

class multiplex(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    city = models.CharField(max_length=30,choices=city_list)
    state = models.CharField(max_length=30,choices=state_list)
    website = models.URLField()

    def __str__(self):
        return self.name

type_list = [
    ('1','2D'),
    ('2','3D'),
    ('3','4DX3D'),
]

language_list = [
    ('1','Hindi'),
    ('2','English'),
    ('3','Gujarati'),
    ('4','Hinglish'),
]

class shows(models.Model):
    moviename=models.ForeignKey(movie,on_delete=models.CASCADE)
    multiplexname = models.ForeignKey(multiplex,on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    seats = models.IntegerField()
    price = models.IntegerField()
    type = models.CharField(max_length=30,choices=type_list)
    language = models.CharField(max_length=30,choices=language_list)

