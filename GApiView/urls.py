from django.urls import path, re_path
from GApiView import views

urlpatterns = [
        path('book/', views.Bookview.as_view()),
        path('publish/', views.Publishview.as_view()),
        re_path(r'publish/(?P<pk>\d+)/', views.PublishDetailview.as_view()),
]
