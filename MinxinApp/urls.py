from django.urls import path ,re_path
from MinxinApp import views

urlpatterns = [
    path('book/', views.Bookview.as_view()),
    re_path(r'book/(?P<pk>\d+)/', views.BookDetail.as_view()),
    re_path(r'publish/(?P<pk>\d+)/', views.PublishDetail.as_view()),
    path('publish/', views.Publishview.as_view()),
]