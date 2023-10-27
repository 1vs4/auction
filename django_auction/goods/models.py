from django.db import models
from django.utils.timezone import now

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='goods_images')
    expiration = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.name

    def is_expired(self):
        return True if now() >= self.expiration else False