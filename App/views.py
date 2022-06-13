from hashlib import new
from django.http import HttpResponse
from django.shortcuts import render
from App.models import Book

# Create your views here.
from rest_framework.views import APIView
from rest_framework import  serializers
from rest_framework.response import Response




class BookSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    price = serializers.IntegerField()
    # 字段重命名
    date = serializers.DateField(source='pub_date')




class Bookview(APIView):
    # get 请求参数数据存放在request.query_params中
    def get(self, request):
        print('query_params:', request.query_params)
        books = Book.objects.all()
        # 构建序列化器对象 : 
        # instance 需要序列化的对象
        # many=True 需要序列化对象内有多个数据
        serializer = BookSerializers(instance=books, many=True)
        return Response(serializer.data)

 
    # # post 请求参数数据存放在request.data中
    def post(self, request):
        # print("data: ", request.data)
        # 创建反序列化器
        serializer = BookSerializers(data=request.data)
        # 校验数据 ： 通过BookSerializers 类字段校验
        if serializer.is_valid():
            new_book = Book.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        # return HttpResponse('post请求')



    
 