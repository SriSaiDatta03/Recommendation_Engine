from django.urls import path
from .views import ProductListView,InteractionView, RecommendationsView

urlpatterns=[
    path('products/',ProductListView.as_view(),name='product-list'),
    path('interactions/',InteractionView.as_view(),name='interaction'),
    path("recommendations/<str:user_id>/", RecommendationsView.as_view(), name="recommendations"),   
    ]