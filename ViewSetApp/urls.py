from ViewSetApp import views
from django.urls import path, re_path

from rest_framework import routers


router = routers.DefaultRouter()
router.register('book',views.BookView)
urlpatterns = []

# urlpatterns = [
#     path('book/', views.BookView.as_view({"get" : "list", "post" : "create",})),
#     re_path(r'book/(?P<pk>\d+)/', views.BookView.as_view({"put" : "update", "get" : "retrieve",  "delete" : "destroy"})),
# ]
urlpatterns += router.urls
