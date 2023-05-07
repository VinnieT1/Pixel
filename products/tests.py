from django.test import TestCase
from products.models import Product

class ProductTestCase(TestCase):
    def test_create_product(self):
        self.assertEqual(Product.objects.count(), 0)

        title = 'Test Product'
        description = 'This is a test product.'
        price = 9.99
        product = Product.objects.create(title=title, description=description, price=price)

        self.assertEqual(product.title, title)
        self.assertEqual(product.description, description)
        self.assertEqual(product.price, price)
        self.assertEqual(Product.objects.count(), 1)
