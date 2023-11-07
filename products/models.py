from django.db import models
from user.models import Users


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Категория: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)



class Basket(models.Model):
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=Users, on_delete= models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete= models.CASCADE)

    objects= BasketQuerySet.as_manager()
    def __str__(self):
        return f'Корзина пользователя {self.user.email}| Продукты: {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

