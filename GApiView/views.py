from multiprocessing import managers
from django.shortcuts import render

from App.models import Book, Publish, Author
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# 继承自APIView
from rest_framework.generics import GenericAPIView


# Create your views here.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Bookview(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(instance=books, many=True)
        return Response(serializer.data)
    

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'

class Publishview(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    def get(self, request):
        # 逻辑重复： 模型类和序列化器
        # publish = Publish.objects.all()
        # serializer = PublishSerializer(instance=publish, many=True)
        # 等同于：
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:   
            return Response(serializer.error)

class PublishDetailview(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    # self.get_object() 以指定变量pk获取值
    def get(self, request, pk):
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
    def delete(self, request, pk):
        self.get_object().delete()
        return Response()