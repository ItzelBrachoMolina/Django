from django.urls import reverse

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500)


# get_absolute_url es para crear una página de detalles del objeto
# Aquí get_absolute_url viene en imagen.
# Le dice a Django dónde ir cuando se crea una nueva publicación.


    def get_absolute_url(self):
        return reverse("food:detail",kwargs={"pk":self.pk})