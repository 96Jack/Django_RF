
# Create your views here.
from multiprocessing import context
from App.models import Book, HeroInfo
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = "__all__"

class BookSerialiers(serializers.ModelSerializer):
    """
    # 书籍： 一  
    # 英雄： 多
    """
    # 返回一对多数据中的单一字段信息 :  从表小写_set(多)
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)

    # 返回从表的多个数据字段内容： 序列化器嵌套
    heroinfo_set = HeroInfoSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
    

class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        ser = BookSerialiers(instance=books, many=True)
        return Response(ser.data)

class HeroView(APIView):
    def get(self, request):
        heros = HeroInfo.objects.all()
        ser = HeroInfoSerializer(instance=heros, many=True)
        # 多查一： 从表(多)小写.外键.主表字段名
        for hero in heros:
            print(hero.hbook.title)

        print(ser.data)
        return Response(ser.data)