from django.db import models
from .categoryModel import Category
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    brand = models.CharField(max_length=50, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=500, default='')
    quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='static/img/products', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Product'

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())
        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


class ProductReviewModel(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'ProductReview'


class CustomerOrders(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'CustomerOrders'


class WaitingListModel(models.Model):
    product = models.ForeignKey(Product, related_name='product_waiting', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_waiting', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'WaitingListModel'
