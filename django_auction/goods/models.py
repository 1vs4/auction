from django.db import models
from django.utils.timezone import now

from users.models import User



class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image1 = models.ImageField(upload_to='goods_images', blank=True)
    image2 = models.ImageField(upload_to='goods_images', blank=True)
    expiration = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True)
    is_active = models.BooleanField(default=True)




    def __str__(self):
        return self.name

    def is_expired(self):
        if now() >= self.expiration:
            if not Order.objects.filter(user=self.user, product=self):
                Order.objects.create(user=self.user, product=self)
            return True
        else:
            return False


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, blank=False)