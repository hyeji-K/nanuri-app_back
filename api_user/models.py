from django.db import models
from django.db.models.expressions import F
import uuid

# Create your models here.
class User(models.Model):
    # user_id = models.CharField(max_length=50, null=False)
    # password = models.CharField(max_length=30, null=False)
    # name = models.CharField(max_length=50, null=False)
    # address = models.CharField(max_length=100, null=False)


    # userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # db의 id랑 겹치는데 왜 때문인지??? 
    userEmail = models.EmailField(max_length=100, unique=True, null=False) # 사용자의 이메일 
    userArea = models.CharField(max_length=100, null=False) # 사용자의 동네 
    userName = models.CharField(max_length=50, unique=True, null=False) # 사용자의 닉네임
    ratingScore = models.IntegerField(default=0, null=True) # 사용자의 점수 
    createdAt = models.DateTimeField(auto_now_add=True, null=False) # 사용자의 가입일
    # activated = models.BooleanField(null=True) # 사용자의 활성화 상태 (1 또는 2)
    userBank = models.CharField(max_length=50, null=True) # 사용자의 은행 이름 
    bankNum = models.IntegerField(null=True) # 사용자의 은행 계좌
    userNumber = models.IntegerField(null=True) # 사용자의 전화번호

    class Meta:
        db_table = "User"


