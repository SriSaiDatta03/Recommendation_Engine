from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products import serializers
from .models import Product,Interaction
from .serializers import ProductSerializer,InteractionSerializer




# Create your views here.
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class InteractionView(APIView):
    def post(self,request):
        serializer=InteractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class RecommendationsView(APIView):
    def get(self, request, user_id):
        try:
            # Get user
            user = User.objects.get(username=user_id)

            # Fetch user interactions
            interactions = Interaction.objects.filter(user=user)

            if not interactions.exists():
                return Response(
                    {"message": f"No interactions found for the user '{user_id}'"},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Generate recommendations based on user interactions
            # Example: Recommend products the user hasn't interacted with
            interacted_products = interactions.values_list('product_id', flat=True)
            recommendations = Product.objects.exclude(id__in=interacted_products)[:10]

            # Serialize and return recommendations
            serialized_recommendations = [
                {"id": product.id, "name": product.name, "category": product.category, "price": product.price}
                for product in recommendations
            ]

            return Response(
                {"user": user.username, "recommendations": serialized_recommendations},
                status=status.HTTP_200_OK
            )

        except User.DoesNotExist:
            return Response(
                {"message": f"User '{user_id}' not found."},
                status=status.HTTP_404_NOT_FOUND
            )