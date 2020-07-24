from django.urls import path
from .views import my_blogs,all_blogs,blog_detail
from .crud_views import Create,Update,Delete
urlpatterns = [
    path('',all_blogs,name="all_blogs"),
    path('<int:blog_id>/',blog_detail,name="blog_detail"),
    path('create/',Create.as_view(),name="blog_create"),
    path('delete/<int:blog_id>/',Delete.as_view(),name="blog_delete"),
    path('update/<int:blog_id>/',Update.as_view(),name="blog_update"),

    path('myblogs/',my_blogs,name="my_blogs")
] 