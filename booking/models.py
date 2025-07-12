from django.db import models
from django.contrib.auth.models import User

class TypeRoom(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title
    

class Room(models.Model):
    number=models.PositiveIntegerField()
    description = models.TextField(null=True,blank=True)
    place=models.PositiveIntegerField(default=1)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to='rooms_images')
    type_room=models.ForeignKey(TypeRoom, on_delete=models.CASCADE)
    def __str__(self):
        return f"Room Number:{self.number}- price:{self.price}- places:{self.place}"
    

class Reservation(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date_start=models.DateTimeField()
    date_end=models.DateTimeField()
    phone=models.CharField(max_length=15)
    persons=models.PositiveIntegerField(default=1)
    created=models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return f"Reservation:{self.pk}- {self.room}- {self.user}- {self.date_start}- {self.date_end}"
    

   



    