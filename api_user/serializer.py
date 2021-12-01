from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Product, Category, User, SocialLogin

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLogin
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'