from django.urls import path
from . import views

urlpatterns = [
      path('', views.shoppingCart),
      path('deleteItem/', views.deleteItem),
]