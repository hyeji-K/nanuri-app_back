from django.urls import path
from . import views

app_name = 'api_user'

urlpatterns = [
    path('users/', views.UserView.as_view()),
    path('users/<int:uid>', views.UserView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('products/<int:uid>', views.ProductView.as_view()),
]