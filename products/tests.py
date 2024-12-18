from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product,Interaction
from django.contrib.auth.models import User

# Create your tests here.

class ProductRecommendationTests(TestCase):
    def setUp(self):
        self.client=APIClient()
        self.user=User.objects.create_user(username='testuser',password='testpass')
        self.product1=Product.objects.create(
            name="Laptop",
            description="A high-performance laptop",
            price=1000.00,
            category="Electronics"  
        )
        self.product2=Product.objects.create(
            name="Tablet",
            description="A lightweight tablet",
            price=300.00,
            category="Electronics"
        )
        self.product3=Product.objects.create(
            name="Book",
            description="A great book",
            price=20.00,
            category="Books"
        )

        self.interaction=Interaction.objects.create(
            user=self.user,
            product=self.product1,
            action="view"
        )

    def test_get_recommendations(self):
        url=reverse('recommend-products',args=[self.user.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(len(response.data)>0)

    def test_no_interactions(self):
        new_user=User.objects.create_user(username='newuser',password='newpass')
        url=reverse('recommend-products',args=[new_user.id])
        response=self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        self.assertIn('No interactions found',response.data['message'])