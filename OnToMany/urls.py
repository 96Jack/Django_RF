from django.urls import  path
from OnToMany import views

urlpatterns = [
    path("book/", views.BookView.as_view()),
    path("hero/", views.HeroView.as_view()),
]