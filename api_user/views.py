from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api_user.models import User
from api_user.serializer import UserSerializer
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
            uid = kwargs.get('uid')
            user_queryset = User.objects.get(id=uid)
            user_serializer = UserSerializer(user_queryset)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

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
