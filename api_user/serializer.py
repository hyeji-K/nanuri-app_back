from typing_extensions import Required
from django.db import models
from django.db.models import fields
from django.http import request
from rest_framework import serializers
from .models import Order, SocialLogin, User, Category, Product, Comment

# 소셜 로그인
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLogin
        fields = '__all__'

class LoginBodySerializer(serializers.Serializer):
    social_id = serializers.IntegerField(help_text="소셜로그인의 유일한 ID 작성")

# 상품
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductPutSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=False)
    link = serializers.URLField(required=False)
    product_image = serializers.CharField(required=False)
    product_price = serializers.IntegerField(required=False)
    total_ppl_cnt = serializers.IntegerField(required=False)
    join_ppl_cnt = serializers.IntegerField(required=False)
    end_date = serializers.DateField(required=False)
    delivery_method = serializers.CharField(required=False)
    detail_content = serializers.CharField(required=False)
    # user_id = serializers.PrimaryKeyRelatedField(required=False)
    # category_id = serializers.PrimaryKeyRelatedField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

class ProductBodySerializer(serializers.Serializer):
    product_name = serializers.CharField(help_text="상품 이름 작성")
    link = serializers.URLField(help_text="상품 URL 작성")
    product_image = serializers.CharField(help_text="상품 이미지 등록")
    product_price = serializers.IntegerField(help_text="상품 가격 작성")
    total_ppl_cnt = serializers.IntegerField(help_text="참가할 수 있는 인원수 작성")
    end_date = serializers.DateField(help_text="마감 날짜 작성")
    delivery_method = serializers.CharField(help_text="전달 방법 작성")
    detail_content = serializers.CharField(help_text="상품 내용 작성")
    user_id = serializers.IntegerField(help_text="등록한 사용자의 ID 작성")
    category_id = serializers.IntegerField(help_text="카테고리 ID 작성")

class ProductBodyPutSerializer(serializers.Serializer):
    # product_name = serializers.CharField(help_text="상품 이름 작성")
    # link = serializers.URLField(help_text="상품 URL 작성")
    # product_image = serializers.CharField(help_text="상품 이미지 등록")
    # product_price = serializers.IntegerField(help_text="상품 가격 작성")
    # total_ppl_cnt = serializers.IntegerField(help_text="참가할 수 있는 인원수 작성")
    join_ppl_cnt = serializers.IntegerField(help_text="참가할 수 있는 인원수 작성")
    # end_date = serializers.DateField(help_text="마감 날짜 작성")
    # delivery_method = serializers.CharField(help_text="전달 방법 작성")
    # detail_content = serializers.CharField(help_text="상품 내용 작성")
    user_id = serializers.IntegerField(help_text="등록한 사용자의 ID 작성")
    category_id = serializers.IntegerField(help_text="카테고리 ID 작성")

# 카테고리
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryEachSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = (
            'category_id',
            'category_name',
            'products'
        )

class CategoryEachSevenSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'category_id',
            # 'category_name',
            'product_id',
            'product_name',
            'link',
            # 'product_image',
            'product_price',
            'total_ppl_cnt',
            'join_ppl_cnt',
            'start_date',
            'end_date',
            'user_id'
        )


class CategoryBodySerializer(serializers.Serializer):
    category_name = serializers.CharField(help_text="카테고리 이름 작성")

# 주문한 상품
class OrderSerializer(serializers.ModelSerializer):
    # product_id = ProductSerializer()

    class Meta:
        model = Order
        fields = (
            'user_id',
            'product_id',
            'credit_method',
            'created_at'
        )

class OrderBodySerializer(serializers.Serializer):
    user_id = serializers.IntegerField(help_text="사용자 ID 작성")
    product_id = serializers.IntegerField(help_text="상품 ID 작성")
    credit_method = serializers.CharField(help_text="구매 방식 작성")

# 사용자
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserPutSerializer(serializers.ModelSerializer):
    user_area = serializers.CharField(required=False)
    user_nick = serializers.CharField(required=False)
    score = serializers.IntegerField(required=False)
    user_bank = serializers.CharField(required=False)
    banknum = serializers.IntegerField(required=False)
    user_number = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = '__all__'

class UserProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    # orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = (
            'user_id',
            'user_area',
            'user_nick',
            'score',
            'user_bank',
            'banknum',
            'user_number',
            'created_at',
            'update_at',
            'social_id',
            'products',
            # 'orders'
        )
        
class UserBodySerializer(serializers.Serializer):
    user_area = serializers.CharField(help_text="사용자의 동네 작성")
    user_nick = serializers.CharField(help_text="사용자의 닉네임 작성")
    social_id = serializers.IntegerField(help_text="소셜로그인 PK 작성")

class EachUserBodySerializer(serializers.Serializer):
    user_area = serializers.CharField(help_text="사용자의 동네 작성")
    user_nick = serializers.CharField(help_text="사용자의 닉네임 작성")
    user_bank = serializers.CharField(help_text="사용자의 은행 등록")
    banknum = serializers.IntegerField(help_text="은행 계좌번호 등록")
    user_number = serializers.IntegerField(help_text="사용자의 폰 번호 등록")
    social_id = serializers.IntegerField(help_text="소셜로그인 PK 작성")

# 댓글
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentBodySerializer(serializers.Serializer):
    content = serializers.CharField(help_text="댓글 내용 작성")
    product_id = serializers.IntegerField(help_text="댓글을 등록하려는 상품 ID 작성")
    user_id = serializers.IntegerField(help_text="댓글을 등록하는 사용자 ID 작성")


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'product_id',
            'product_name',
            'link',
            'product_image',
            'product_price',
            'total_ppl_cnt',
            'join_ppl_cnt',
            'start_date',
            'end_date',
            'user_id'
        )
