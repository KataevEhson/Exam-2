from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Category(models.Model):
    title = models.TextField()
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)



class Stadium(models.Model):
    caption = models.TextField()
    location = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateField(default=datetime.now)
    is_free = models.BooleanField(default=True)




class My_booked_stadium(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = models.DateField(default=datetime.now)
    time_end = models.CharField()
    playears_needad = models.IntegerField()
    created_at = models.DateField(default=datetime.now)
    status = models.BooleanField(default=False)    



class Particplant(models.Model):
    booking =  models.ForeignKey(My_booked_stadium, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joinad_at = models.DateField(default=datetime.now)