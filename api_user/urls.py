from django.urls import path
from . import views

app_name = 'api_user'

urlpatterns = [
    path('logins/', views.LoginView.as_view()),
    path('logins/<int:id>', views.EachLoginView.as_view()),
    path('users/', views.UserView.as_view()),
    path('users/<int:user_id>', views.EachUserView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('category/<int:category_id>', views.EachCategoryView.as_view()),
    # path('category/<str:slug>/', views.category_page),
    # path('users/<int:uid>/regiproducts/', views.ProductView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('products/<int:uid>', views.EachProductView.as_view()),
    path('comment/', views.CommentView.as_view()),
    path('comment/<int:product_id>', views.EachCommentView.as_view()),
]