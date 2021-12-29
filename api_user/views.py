from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api_user.models import SocialLogin, User, Category, Product, Comment, Order
from api_user.serializer import LoginSerializer, UserSerializer, CategorySerializer, ProductSerializer, CommentSerializer, CategoryBodySerializer, CommentBodySerializer, LoginBodySerializer, ProductBodySerializer, UserBodySerializer, EachUserBodySerializer, OrderSerializer, OrderBodySerializer, CategoryEachSerializer, UserProductsSerializer
from rest_framework import serializers, status

#swagger
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class LoginView(APIView):
    @swagger_auto_schema(request_body=LoginBodySerializer, operation_summary="Add SocialLogin ID")
    def post(self, request):
        """
            소셜로그인 정보를 등록하는 API
            ---
            ### 내용
            - ### id : PK
            - ### social_id : 소셜로그인의 ID
        """
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            login_serializer.save()
            return Response({'create':'success', 'data':login_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'create':'fail', 'error':login_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Returns all SocialLogin ID")
    def get(self, request):
        """
            소셜로그인 정보를 불러오는 API
            ---
            ### 내용
            - ### id : PK
            - ### social_id : 소셜로그인의 ID
        """
        login_queryset = SocialLogin.objects.all()
        login_serializer = LoginSerializer(login_queryset, many=True)
        return Response({'count':login_queryset.count(), 'data':login_serializer.data}, status=status.HTTP_200_OK)
    
class EachLoginView(APIView):
    # 나중에 수정
    @swagger_auto_schema(operation_summary="Delete a SocialLogin ID")
    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response({'delete':'fail', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = kwargs.get('id')
            login_object = SocialLogin.objects.get(id=id)
            login_object.delete()
            return Response({'delete':'success', 'message':"delete ok"}, status=status.HTTP_200_OK)


class UserView(APIView):
    @swagger_auto_schema(request_body=UserBodySerializer, operation_summary="Add user")
    def post(self, request):
        """
            회원 정보를 불러오는 API
            ---
            ### 내용
            - ### user_id : 사용자의 UUID
            - ### user_area : 사용자의 동네 
            - ### user_nick : 사용자의 닉네임
            - ### social_id : 소셜로그인 PK
        """
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'create':'success', 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'create':'fail', 'error':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Returns all user")
    def get(self, request, **kwargs):
        """
            회원 정보를 불러오는 API
            ---
            ### 내용
            - ### user_id : 사용자의 UUID
            - ### user_area : 사용자의 동네 
            - ### user_nick : 사용자의 닉네임
            - ### score : 사용자의 평가점수
            - ### user_bank : 사용자의 은행
            - ### banknum : 사용자의 은행 계좌번호
            - ### user_number : 사용자의 폰 번호
            - ### created_at : 사용자의 가입 날짜
            - ### update_at : 사용자 정보 변경 날짜
            - ### social_id : 소셜로그인 PK
        """
        user_queryset = User.objects.all()
        user_serializer = UserSerializer(user_queryset, many=True)
        return Response({'count':user_queryset.count(), 'data':user_serializer.data}, status=status.HTTP_200_OK)
        
class EachUserView(APIView):
    @swagger_auto_schema(operation_summary="Find a user by user id")
    def get(self, request, **kwargs):
        """
            회원 정보를 불러오는 API
            ---
            ### 내용
            - ### user_id : 사용자의 UUID
            - ### user_area : 사용자의 동네 
            - ### user_nick : 사용자의 닉네임
            - ### score : 사용자의 평가점수
            - ### user_bank : 사용자의 은행
            - ### banknum : 사용자의 은행 계좌번호
            - ### user_number : 사용자의 폰 번호
            - ### created_at : 사용자의 가입 날짜
            - ### update_at : 사용자 정보 변경 날짜
            - ### social_id : 소셜로그인 PK
        """
        if kwargs.get('user_id') is None:
            user_queryset = User.objects.all()
            user_serializer = UserSerializer(user_queryset, many=True)
            return Response({'count':user_queryset.count(), 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('user_id')
            user_queryset = UserProductsSerializer(User.objects.get(user_id=id))

            # 구매한 상품
            product_count = Order.objects.filter(user_id=id).values_list('product_id', flat=True) # [1, 2, 3]
            order_product = []
            for i in product_count:
                product = Product.objects.filter(product_id=i)
                product_serializer = ProductSerializer(product, many=True)
                order_product.extend(product_serializer.data)

            return Response({'user':user_queryset.data, 'orders':order_product}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EachUserBodySerializer, operation_summary="Update a user by user id")
    def put(self, request, **kwargs):
        """
            회원 정보를 수정하는 API
            ---
            ### 내용
            - ### user_id : 사용자의 UUID
            - ### user_area : 사용자의 동네 
            - ### user_nick : 사용자의 닉네임
            - ### user_bank : 사용자의 은행
            - ### banknum : 사용자의 은행 계좌번호
            - ### user_number : 사용자의 폰 번호
            - ### social_id : 소셜로그인 PK
        """
        if kwargs.get('user_id') is None:
            return Response({'result':'fail', 'error':"Invalid request"}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = kwargs.get('user_id')
            user_object = User.objects.get(user_id=id)
            # product_object = Product.objects.get(user_id=id)
            update_serializer = UserSerializer(user_object, data=request.data)
            # update_product_serializer = ProductSerializer(product_object, data=request.data)

            if update_serializer.is_valid():
                update_serializer.save()
                return Response({'update':'success', 'data':update_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'update':'fail', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_summary="Delete a user")
    def delete(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            return Response({'delete':'fail', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = kwargs.get('user_id')
            user_object = User.objects.get(user_id=id)
            user_object.delete()
            return Response({'delete':'success', 'message':"delete ok"}, status=status.HTTP_200_OK)


# Category
class CategoryView(APIView):
    @swagger_auto_schema(request_body=CategoryBodySerializer, 
                            responses={200: '성공', 403: '인증에러', 400: '입력값 유효성 검증 실패', 500: '서버에러'}, 
                            operation_summary="Add a new category")
    def post(self, request):
        """
            카테고리를 생성하는 API
            ---
            ### 내용
            - ### category_id : 카테고리의 ID
            - ### category_name : 카테고리 이름
        """
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':category_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Returns all category")
    def get(self, request):
        """
            카테고리를 불러오는 API
            ---
            ### 내용
            - ### category_id : 카테고리의 ID
            - ### category_name : 카테고리 이름
        """
        category_queryset = Category.objects.all().order_by('category_id')
        category_serializer = CategorySerializer(category_queryset, many=True)
        return Response({'count':category_queryset.count(), 'categorys':category_serializer.data}, status=status.HTTP_200_OK)
        
# 각 카테고리 별 상품 보여주기
class EachCategoryView(APIView):
    @swagger_auto_schema(operation_summary="Find products by category ID")
    def get(self, request, **kwargs):
        if kwargs.get('category_id') is None:
            category_queryset = Category.objects.all()
            category_serializer = CategorySerializer(category_queryset, many=True)
            return Response({'count':category_queryset.count(), 'categorys':category_serializer.data}, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('category_id')
            category_serializer = CategoryEachSerializer(Category.objects.get(category_id=id))
            return Response({'category':category_serializer.data}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_summary="Delete a category by category ID")
    def delete(self, request, **kwargs):
        """
            카테고리를 삭제하는 API
            ---
            ### 내용
            - ### category_id : 카테고리의 ID
            - ### category_name : 카테고리 이름
        """
        if kwargs.get('category_id') is None:
            return Response({'delete':'fail', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = kwargs.get('category_id')
            category_object = Category.objects.get(category_id=id)
            category_object.delete()
            return Response({'delete':'success', 'message':"delete ok"}, status=status.HTTP_200_OK)

# Product
class ProductView(APIView):
    @swagger_auto_schema(request_body=ProductBodySerializer, operation_summary="Add product")
    def post(self, request):
        """
            상품을 등록하는 API
            ---
            ### 내용
            - ### product_id : 상품의 ID
            - ### product_name : 상품 이름
            - ### link : 상품 URL
            - ### product_image : 상품 이미지
            - ### product_price : 상품 가격
            - ### total_ppl_cnt : 공동구매 참여할 수 있는 인원수
            - ### join_ppl_cnt : 공동구매에 참여한 인원수
            - ### start_date : 공동구매 시작일
            - ### end_date : 공동구매 마감일
            - ### delivery_method : 전달 방법
            - ### detail_content : 상품에 대한 자세한 내용
            - ### create_at : 상품 등록 날짜
            - ### update_at : 업데이트 날짜
            - ### user_id : 상품을 등록한 사용자 ID
            - ### category_id : 상품의 카테고리 ID
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'true', 'products':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Find all product")
    def get(self, request):
        """
            상품을 불러오는 API
            ---
            ### 내용
            - ### product_id : 상품의 ID
            - ### product_name : 상품 이름
            - ### link : 상품 URL
            - ### product_image : 상품 이미지
            - ### product_price : 상품 가격
            - ### total_ppl_cnt : 공동구매 참여할 수 있는 인원수
            - ### join_ppl_cnt : 공동구매에 참여한 인원수
            - ### start_date : 공동구매 시작일
            - ### end_date : 공동구매 마감일
            - ### delivery_method : 전달 방법
            - ### detail_content : 상품에 대한 자세한 내용
            - ### create_at : 상품 등록 날짜
            - ### update_at : 업데이트 날짜
            - ### user_id : 상품을 등록한 사용자 ID
            - ### category_id : 상품의 카테고리 ID
        """
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count':queryset.count(), 'products':serializer.data}, status=status.HTTP_200_OK)

class EachProductView(APIView):
    @swagger_auto_schema(operation_summary="Find a product by product ID")
    def get(self, request, **kwargs):
        """
            상품을 불러오는 API
            ---
            ### 내용
            - ### product_id : 상품의 ID
            - ### product_name : 상품 이름
            - ### link : 상품 URL
            - ### product_image : 상품 이미지
            - ### product_price : 상품 가격
            - ### total_ppl_cnt : 공동구매 참여할 수 있는 인원수
            - ### join_ppl_cnt : 공동구매에 참여한 인원수
            - ### start_date : 공동구매 시작일
            - ### end_date : 공동구매 마감일
            - ### delivery_method : 전달 방법
            - ### detail_content : 상품에 대한 자세한 내용
            - ### create_at : 상품 등록 날짜
            - ### update_at : 업데이트 날짜
            - ### user_id : 상품을 등록한 사용자 ID
            - ### category_id : 상품의 카테고리 ID
        """
        if kwargs.get('product_id') is None:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response({'count':queryset.count(), 'products':serializer.data}, status=status.HTTP_200_OK)
        else:
            uid = kwargs.get('product_id')
            object = Product.objects.filter(product_id=uid)
            product_serializer = ProductSerializer(object, many=True)
            return Response({'products':product_serializer.data}, status=status.HTTP_200_OK)

    # @swagger_auto_schema(operation_summary="Update a product by product ID")
    # def put(self, request, **kwargs):
    #     """
    #         상품을 수정하는 API
    #         ---
    #         ### 내용
    #         - ### product_id : 상품의 ID
    #         - ### product_name : 상품 이름
    #         - ### link : 상품 URL
    #         - ### product_image : 상품 이미지
    #         - ### product_price : 상품 가격
    #         - ### total_ppl_cnt : 공동구매 참여할 수 있는 인원수
    #         - ### join_ppl_cnt : 공동구매에 참여한 인원수
    #         - ### start_date : 공동구매 시작일
    #         - ### end_date : 공동구매 마감일
    #         - ### delivery_method : 전달 방법
    #         - ### detail_content : 상품에 대한 자세한 내용
    #         - ### create_at : 상품 등록 날짜
    #         - ### update_at : 업데이트 날짜
    #         - ### user_id : 상품을 등록한 사용자 ID
    #         - ### category_id : 상품의 카테고리 ID
    #     """
    #     if kwargs.get('uid') is None:
    #         return Response({'success':'false', 'error':"Invalid request"}, status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         uid = kwargs.get('uid')
    #         object = Product.objects.get(product_id=uid)
    #         update_serializer = ProductSerializer(object, data=request.data)
    #         if update_serializer.is_valid():
    #             update_serializer.save()
    #             return Response({'update':'true', 'data':update_serializer.data}, status=status.HTTP_200_OK)
    #         else:
    #             return Response({'update':'false', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(operation_summary="Delete a product by product ID")
    def delete(self, request, **kwargs):
        """
            상품을 삭제하는 API
            ---
            ### 내용
            - ### product_id : 상품의 ID
            - ### product_name : 상품 이름
            - ### link : 상품 URL
            - ### product_image : 상품 이미지
            - ### product_price : 상품 가격
            - ### total_ppl_cnt : 공동구매 참여할 수 있는 인원수
            - ### join_ppl_cnt : 공동구매에 참여한 인원수
            - ### start_date : 공동구매 시작일
            - ### end_date : 공동구매 마감일
            - ### delivery_method : 전달 방법
            - ### detail_content : 상품에 대한 자세한 내용
            - ### create_at : 상품 등록 날짜
            - ### update_at : 업데이트 날짜
            - ### user_id : 상품을 등록한 사용자 ID
            - ### category_id : 상품의 카테고리 ID
        """
        if kwargs.get('product_id') is None:
            return Response({'delete':'false', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)
        else:
            uid = kwargs.get('product_id')
            object = Product.objects.get(product_id=uid)
            object.delete()
            return Response({'delete':'true', 'message':"delete ok"}, status=status.HTTP_200_OK)


class CommentView(APIView):
    @swagger_auto_schema(operation_summary="Returns all comment")
    def get(self, request):
        """
            댓글을 불러오는 API
            ---
            ### 내용
            - ### comment_id : 댓글의 ID
            - ### content : 댓글 내용
            - ### created_at : 댓글 생성 날짜
            - ### product_id : 댓글을 등록하려는 상품 ID
            - ### user_id : 댓글을 등록하는 사용자 ID
        """
        comment_queryset = Comment.objects.all()
        comment_serializer = CommentSerializer(comment_queryset, many=True)
        return Response({'count':comment_queryset.count(), 'comments':comment_serializer.data}, status=status.HTTP_200_OK)
        
    @swagger_auto_schema(request_body=CommentBodySerializer, operation_summary="Add comment")
    def post(self, request):
        """
            댓글을 생성하는 API
            ---
            ### 내용
            - ### comment_id : 댓글의 ID
            - ### content : 댓글 내용
            - ### created_at : 댓글 생성 날짜
            - ### product_id : 댓글을 등록하려는 상품 ID
            - ### user_id : 댓글을 등록하는 사용자 ID
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'true', 'comments':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EachCommentView(APIView):
    @swagger_auto_schema(operation_summary="Find comments by product ID")
    def get(self, request, **kwargs):
        """
            상품 ID에 따른 댓글을 불러오는 API
            ---
            ### 내용
            - ### comment_id : 댓글의 ID
            - ### content : 댓글 내용
            - ### created_at : 댓글 생성 날짜
            - ### product_id : 댓글을 등록하려는 상품 ID
            - ### user_id : 댓글을 등록하는 사용자 ID
        """
        if kwargs.get('product_id') is None:
            comment_queryset = Comment.objects.all()
            comment_serializer = CommentSerializer(comment_queryset, many=True)
            return Response({'count':comment_queryset.count(), 'comments':comment_serializer.data}, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('product_id')
            comment_serializer = CommentSerializer(Comment.objects.get(product_id=id))
            return Response({'comments':comment_serializer.data}, status=status.HTTP_200_OK)

class OrderView(APIView):
    @swagger_auto_schema(operation_summary="Find a order by product id")
    def get(self, request, **kwargs):
        """
            user ID에 따른 상품을 주문하는 API
            ---
            ### 내용
            - ### user_id : 상품 주문을 하는 사용자 ID
            - ### product_id : 주문하려는 상품 ID
            - ### credit_method : 주문 방법(카드 or 계좌)
            - ### created_at : 주문 날짜
        """
        if kwargs.get('user_id') is None:
            order_queryset = Order.objects.all().order_by('user_id')
            order_serializer = OrderSerializer(order_queryset, many=True)
            return Response({'count':order_queryset.count(), 'order':order_serializer.data}, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('user_id')
            # 구매한 상품
            # products = Order.objects.filter(user_id=id).select_related('Products').values()
            orders = Order.objects.filter(user_id=id)
            order_serializer = OrderSerializer(orders, many=True)
            pro = Order.objects.filter(user_id=id).values_list('product_id', flat=True) # [1, 2, 3]
            order_product = []
            for i in pro:
                product = Product.objects.filter(product_id=i)
                product_serializer = ProductSerializer(product, many=True)
                order_product.extend(product_serializer.data)
            return Response({'count':orders.count(), 'products':order_product}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=OrderBodySerializer, operation_summary="Add comment")
    def post(self, request):
        """
            user ID에 따른 상품을 주문하는 API
            ---
            ### 내용
            - ### user_id : 상품 주문을 하는 사용자 ID
            - ### product_id : 주문하려는 상품 ID
            - ### credit_method : 주문 방법(카드 or 계좌)
        """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'true', 'comments':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
