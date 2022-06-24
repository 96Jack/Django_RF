from django.shortcuts import render

from App.models import Book
from rest_framework import serializers
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# 继承APIView， 那么混合类minxins及GenericView用不了了
# class BookView(ViewSet):
#     def get_all(self, request):
#         return Response("查看所有资源")

#     def post_all(self, request):
#         return Response("增加资源")

#     def get_object(self, request, pk):
#         return Response("查看单一资源")

#     def put_object(self, request, pk):
#         return Response('修改单一资源')

#     def delete_object(self, request, pk):
#         return Response("删除资源")



# class BookView(GenericViewSet, ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # 认证
    # authentication_classes = (BasicAuthentication, SessionAuthentication)
    # # 权限： 元组
    # permission_classes = (IsAuthenticated,)
