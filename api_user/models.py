from django.db import models
from django.db.models.expressions import F
import uuid

from django.db.models.fields import AutoField

# Create your models here.
class SocialLogin(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    social_id = models.CharField(max_length=128, null=False, unique=True)

    class Meta:
        db_table = "SocialLogin"

class User(models.Model):
    # userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # db의 id랑 겹치는데 왜 때문인지??? 
    user_id = models.AutoField(primary_key=True, null=False, unique=True)
    # user_email = models.EmailField(max_length=128, unique=True, null=False) # 사용자의 이메일 
    user_area = models.CharField(max_length=128, null=False) # 사용자의 동네 
    user_nick = models.CharField(max_length=128, unique=True, null=False) # 사용자의 닉네임
    score = models.IntegerField(default=0, null=True) # 사용자의 점수 
    user_bank = models.CharField(max_length=32, blank=True, null=True) # 사용자의 은행 이름 
    banknum = models.IntegerField(blank=True, null=True) # 사용자의 은행 계좌
    user_number = models.IntegerField(blank=True, null=True) # 사용자의 전화번호
    created_date = models.DateTimeField(auto_now_add=True, null=False) # 사용자의 가입일
    modify_date = models.DateTimeField(auto_now=True) # 수정 날짜
    # activated = models.BooleanField(null=True) # 사용자의 활성화 상태 (0 또는 1) 로그인하면 1 탈퇴하면 0

    social_id = models.ForeignKey(SocialLogin, null=False, on_delete=models.CASCADE, db_column='social_id')
    
    class Meta:
        db_table = "User"

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False)
    category_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = "Categoey"

class Product(models.Model):
    # no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = AutoField(primary_key=True, null=False, unique=True)
    product_name = models.CharField(max_length=100, null=False)
    link = models.URLField(max_length=200, null=True)
    # productImage = models.ImageField(up) # 이미지는 나중에 허허 .. 
    product_price = models.IntegerField(null=False)
    total_ppl_cnt = models.IntegerField(null=True)
    join_ppl_cnt = models.IntegerField(null=True, default=1)
    start_date = models.DateField(auto_now_add=True, null=False)
    end_date = models.DateField(null=False)
    delivery_method = models.CharField(max_length=10, null=False)
    detail_content = models.CharField(max_length=200, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    modify_date = models.DateTimeField(auto_now=True)
    # activated = models.BooleanField # 활성화 상태

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"



# class BuyProductList(models.Model):
#     pass
