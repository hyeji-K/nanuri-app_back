from django.db import models
from django.db.models.expressions import F
import uuid

from django.db.models.fields import AutoField

# Create your models here.
# 소셜로그인 테이블
class SocialLogin(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    social_id = models.CharField(max_length=128, null=False, unique=True)
    # social_type = models.CharField(max_length=128, null=False)

    class Meta:
        db_table = "SocialLogin"

# 회원 관리 테이블
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
    created_at = models.DateTimeField(auto_now_add=True, null=False) # 사용자의 가입일
    update_at = models.DateTimeField(auto_now=True) # 수정 날짜
    # activated = models.BooleanField(null=True) # 사용자의 활성화 상태 (0 또는 1) 로그인하면 1 탈퇴하면 0

    social_id = models.ForeignKey(SocialLogin, null=False, on_delete=models.CASCADE, db_column='social_id')
    
    class Meta:
        db_table = "User"

# 카테고리 테이블
class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False)
    category_name = models.CharField(max_length=50, null=False, unique=True)
    # slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    # def get_absolute_url(self):
    #     return f'/category/{self.slug}/'

    class Meta:
        db_table = "Categories"

# 상품 등록 테이블
class Product(models.Model):
    # no = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = AutoField(primary_key=True, null=False, unique=True)
    product_name = models.CharField(max_length=100, null=False)
    link = models.URLField(max_length=1000, null=True)
    # productImage = models.ImageField(up) # 이미지는 일단 charfield로 
    product_image = models.CharField(max_length=400, null=True)
    product_price = models.IntegerField(null=False) # default=0 추가?? 
    total_ppl_cnt = models.IntegerField(null=True)
    join_ppl_cnt = models.IntegerField(null=True, default=1)
    start_date = models.DateField(auto_now_add=True, null=False)
    end_date = models.DateField(null=False)
    delivery_method = models.CharField(max_length=10, null=False)
    detail_content = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True)
    # activated = models.BooleanField # 활성화 상태
    # 유저의 동네 정보를 가져와서 상품 테이블에 저장을 해야 동네별로 상품을 보여줄 수 있지 않을까?

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    category_id = models.ForeignKey(Category, db_column='category_id', on_delete=models.CASCADE)

    class Meta:
        db_table = "Product"


# 댓글 테이블
# 상품에 따른 댓글
class Comment(models.Model):
    comment_id = AutoField(primary_key=True, null=False, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Comment"


# # 알림 테이블
# # 관심등록, 댓글, 공동구매 참여에 대한 알림
# # 내가 등록한 상품에 대해서 관심등록을 누르면 "user_name"가 "product"에 관심등록 하였습니다. 
# # 내가 등록한 상품에 대해서 댓글을 달면 "user_name"이 어떤 상품에 댓글을 달았습니다.
# # 내가 등록한 상품에 대해서 공동구매에 참여했다면 "user_name"이 어떤 상품에 대해서 참여했습니다.
# class Alarm(models.Model):
#     alarm_id = models.AutoField(primary_key=True, null=False, unique=True)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField() # 읽기 여부

#     class Meta:
#         db_table = "Alarm"

# class BuyProductList(models.Model):
#     pass
