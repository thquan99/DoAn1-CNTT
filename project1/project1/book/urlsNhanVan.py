from django.urls import path
from . import views

urlpatterns = [
      path('', views.list3),
      path('book/<int:id>/', views.eachItem),    
      path('book/<int:id>/addcart/', views.addcart),
      path('shoppingCart/', views.shoppingCart), 
      path('book/<int:id>/deleteItem/', views.deleteItem),
]