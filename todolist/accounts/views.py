from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.reverse import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import (UserCreateSerializer, UserLoginSerializer, TaskCreateSerializer,
                            ListTaskSerializer, UpdateStatuskSerializer) 
from .models import TaskAll
# Create your views here.

User = get_user_model()

class UserCreateApiView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

class UserLoginApiView(APIView):
    #permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_data = serializer.data
            return HttpResponseRedirect('/api/users/list/')
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ListTaskApiView(APIView):
    #permission_classes = [AllowAny]
    serializer_class = TaskCreateSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        full_data = []
        queryset = TaskAll.objects.all()
        print(queryset)
        for task in queryset:
            temp_data ={
                'id': task.id,
                'task': task.task,
                'created': task.created,
                'finished': task.finished,
                'status': task.status,
            }
            full_data.append(temp_data)
        return Response(full_data, status=HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = TaskCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            task_data = serializer.data
            save_data = TaskAll(task=task_data['task'], finished=task_data['finished'])
            save_data.save()
            return Response(task_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdateStatusApiView(RetrieveUpdateAPIView):
    queryset = TaskAll.objects.all()
    serializer_class = UpdateStatuskSerializer
    lookup_field = 'id'