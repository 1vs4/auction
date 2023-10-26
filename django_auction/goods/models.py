from django.db import models
from django.utils.timezone import now


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='goods_images')
    expiration = models.DateTimeField()

    def __str__(self):
        return self.name

    def is_expired(self):
        return True if now() >= self.expiration else False