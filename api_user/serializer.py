from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import SocialLogin, User, Category, Product, Comment

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLogin
        fields = '__all__'

class LoginBodySerializer(serializers.Serializer):
    social_id = serializers.CharField(help_text="소셜로그인의 유일한 ID 작성")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserBodySerializer(serializers.Serializer):
    user_area = serializers.CharField(help_text="사용자의 동네 작성")
    user_nick = serializers.CharField(help_text="사용자의 닉네임 작성")
    user_bank = serializers.CharField(help_text="사용자의 은행 등록")
    banknum = serializers.CharField(help_text="은행 계좌번호 등록")
    user_number = serializers.CharField(help_text="사용자의 폰 번호 등록")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryBodySerializer(serializers.Serializer):
    category_name = serializers.CharField(help_text="카테고리 이름 작성")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductBodySerializer(serializers.Serializer):
    product_name = serializers.CharField(help_text="상품 이름 작성")
    link = serializers.CharField(help_text="상품 URL 작성")
    product_image = serializers.CharField(help_text="상품 이미지 등록")
    product_price = serializers.CharField(help_text="상품 가격 작성")
    total_ppl_cnt = serializers.CharField(help_text="참가할 수 있는 인원수 작성")
    end_date = serializers.CharField(help_text="마감 날짜 작성")
    delivery_method = serializers.CharField(help_text="전달 방법 작성")
    detail_content = serializers.CharField(help_text="상품 내용 작성")
    user_id = serializers.CharField(help_text="등록한 사용자의 ID 작성")
    category_id = serializers.CharField(help_text="카테고리 ID 작성")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentBodySerializer(serializers.Serializer):
    content = serializers.CharField(help_text="댓글 내용 작성")
    product_id = serializers.CharField(help_text="댓글을 등록하려는 상품 ID 작성")
    user_id = serializers.CharField(help_text="댓글을 등록하는 사용자 ID 작성")