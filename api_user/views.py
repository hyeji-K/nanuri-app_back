from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api_user.models import User, Product
from api_user.serializer import UserSerializer, ProductSerializer
from rest_framework import status

# Create your views here.

class UserView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'success':'true', 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('uid') is None:
            user_queryset = User.objects.all()
            user_serializer = UserSerializer(user_queryset, many=True)
            return Response({'count':user_queryset.count(), 'data':user_serializer.data}, status=status.HTTP_200_OK)
        else:
            sno = kwargs.get('uid')
            user_queryset = UserSerializer(User.objects.get(id=sno))
            # 등록한 상품
            products = Product.objects.filter(user_id=sno)
            product_serializer = ProductSerializer(products, many=True)
            return Response({'user':user_queryset.data, 'products':product_serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('uid') is None:
            return Response({'success':'false', 'error':"Invalid request"}, status=status.HTTP_404_NOT_FOUND)
        else:
            uid = kwargs.get('uid')
            user_object = User.objects.get(id=uid)
            update_serializer = UserSerializer(user_object, data=request.data)
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
            user_object = User.objects.get(id=uid)
            user_object.delete()
            return Response({'delete':'true', 'message':"delete ok"}, status=status.HTTP_200_OK)


# Product
class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'true', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'success':'false', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# product의 id로 조회는 상관없지 않나 
    def get(self, request, **kwargs):
        if kwargs.get('uid') is None:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            return Response({'count':queryset.count(), 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            uid = kwargs.get('uid')
            queryset = Product.objects.get(id=uid)
            serializer = ProductSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

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
