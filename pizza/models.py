from django.db import models
from django.contrib.auth.models import User
# Create your models

class Pizza(models.Model):
    SIZE = (
    ('25cm','25cm'),
    ('35cm','35cm'),
    ('45cm','45cm'),
    )
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, choices=SIZE)
    img = models.ImageField(upload_to='pizza/')
    price = models.FloatField(defaul=0)
    ingredients = models.TextField

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Cooking', 'Cooking'),
        ('Delivered', 'Delivered'),
    )
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='Pending')

    def __str__(self):
        return self.user.username