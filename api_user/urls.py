from django.urls import path
from . import views

app_name = 'api_user'

urlpatterns = [
    path('logins/', views.LoginView.as_view()),
    path('logins/<int:id>', views.LoginView.as_view()),
    path('users/', views.UserView.as_view()),
    path('users/<int:user_id>', views.UserView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('category/<int:category_id>', views.CategoryView.as_view()),
    # path('users/<int:uid>/regiproducts/', views.ProductView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('products/<int:uid>', views.ProductView.as_view()),
]