from django.forms import fields_for_model
from django.shortcuts import render

from App.models import Book, Publish
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin,  DestroyModelMixin, RetrieveModelMixin


# Create your views here.
class serializer_class(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Bookview(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = serializer_class

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)
       
class BookDetail(Bookview, GenericAPIView):
    def get(self, request, pk):
        serializer = self.get_serializer(insyance=self.get_object(), many=False)
        return Response(serializer.data)


#############################基于mixins###################################################################

# class PublishSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = '__all__'   


# class Publishview(ListModelMixin, CreateModelMixin , GenericAPIView):
#     queryset = Publish.objects.all()
#     serializer_class = PublishSerializer
#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


    
# class PublishDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
#     queryset = Publish.objects.all()
#     serializer_class = PublishSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

########################################generics#########################################################
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'   


class Publishview(ListCreateAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


    
class PublishDetail(RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
