from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api_user.models import Product, Category, User, SocialLogin
from api_user.serializer import ProductSerializer, CategorySerializer, UserSerializer, LoginSerializer
from rest_framework import serializers, status

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        login_serializer = LoginSerializer(data=request.data)
        if login_serializer.is_valid():
            login_serializer.save()
            return Response({'create':'success', 'data':login_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'create':'fail', 'error':login_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        login_queryset = SocialLogin.objects.all()
        login_serializer = LoginSerializer(login_queryset, many=True)
        return Response({'count':login_queryset.count(), 'data':login_serializer.data}, status=status.HTTP_200_OK)
    
    # 나중에 수정
    def delete(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response({'delete':'fail', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = kwargs.get('id')
            login_object = SocialLogin.objects.get(id=id)
            login_object.delete()
            return Response({'delete':'success', 'message':"delete ok"}, status=status.HTTP_200_OK)


class UserView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'create':'success', 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'create':'fail', 'error':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            user_queryset = User.objects.all()
            user_serializer = UserSerializer(user_queryset, many=True)
            return Response({'count':user_queryset.count(), 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('user_id')
            user_queryset = UserSerializer(User.objects.get(user_id=id))

            # return Response({'user':user_queryset.data}, status=status.HTTP_200_OK)

            # 등록한 상품
            products = Product.objects.filter(user_id=id)
            product_serializer = ProductSerializer(products, many=True)
            return Response({'user':user_queryset.data, 'products':product_serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('user_id') is None:
            return Response({'result':'fail', 'error':"Invalid request"}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = kwargs.get('user_id')
            user_object = User.objects.get(user_id=id)
            update_serializer = UserSerializer(user_object, data=request.data)
            if update_serializer.is_valid():
                update_serializer.save()
                return Response({'update':'success', 'data':update_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'update':'fail', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)

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
    # 카테고리 추가 완
    # def post(self, request):
    #     category_serializer = CategorySerializer(data=request.data)
    #     if category_serializer.is_valid():
    #         category_serializer.save()
    #         return Response(category_serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'success':'false', 'error':category_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('category_id') is None:
            category_queryset = Category.objects.all()
            category_serializer = CategorySerializer(category_queryset, many=True)
            return Response({'count':category_queryset.count(), 'categorys':category_serializer.data}, status=status.HTTP_200_OK)
        else:
            id = kwargs.get('category_id')
            category_serializer = CategorySerializer(Category.objects.get(category_id=id))
            # 등록한 상품
            products = Product.objects.filter(category_id=id)
            product_serializer = ProductSerializer(products, many=True)
            return Response({'category':category_serializer.data, 'products':product_serializer.data}, status=status.HTTP_200_OK)


# Product
class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'true', 'products':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({'count':queryset.count(), 'products':serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response({'success':'false', 'error':"Invalid request"}, status=status.HTTP_404_NOT_FOUND)
        else:
            uid = kwargs.get('uid')
            object = Product.objects.get(id=uid)
            update_serializer = ProductSerializer(object, data=request.data)
            if update_serializer.is_valid():
                update_serializer.save()
                return Response({'update':'true', 'data':update_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'update':'false', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response({'delete':'false', 'error':"Invalid request".data}, status=status.HTTP_404_NOT_FOUND)
        else:
            uid = kwargs.get('uid')
            object = Product.objects.get(id=uid)
            object.delete()
            return Response({'delete':'true', 'message':"delete ok"}, status=status.HTTP_200_OK)
