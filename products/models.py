from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('CPU', 'CPU'),
        ('GPU', 'GPU'),
        ('PC', 'PC'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title