from django.db import models
from nomduprojet.settings import AUTH_USER_MODEL
# Create your models here.
class Produit(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank =True)
    tsumbnail= models.ImageField(upload_to="products", blank=True, null=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    Order = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.produit.name} ({self.quantity})" 


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)


    def __str__ (self):
        return self.user.username 
