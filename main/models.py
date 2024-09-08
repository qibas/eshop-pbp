from django.db import models

# Create your models here.

class data(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()

    @property # menambah atribut read-only
    def pricelist(self):
        return self.price > 1000000