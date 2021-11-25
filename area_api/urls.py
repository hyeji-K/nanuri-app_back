from django.urls import path
from . import views

app_name = 'area_api'

urlpatterns = [
    path('users/', views.AreaView.as_view()),
]