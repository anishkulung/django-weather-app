from django.test import TestCase
from report.models import Product, ProductDetail

class TestModels(TestCase):
    def setUp(self):
        self.product_name = "Petrol"
        self.year =2020
        self.sales = 123456.78
        self.Product_obj = Product.objects.create(product_name=self.product_name)
        self.ProductDetail_obj = ProductDetail.objects.create(year=self.year, product=self.Product_obj,sales=self.sales)

    def test_Product_returned_string(self):
        self.assertEqual(self.product_name,str(self.Product_obj))

    def test_ProductDetail_returned_string(self):
        self.assertEqual(f"{self.product_name} - {self.year}",str(self.ProductDetail_obj))