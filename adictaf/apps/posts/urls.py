from django.urls import path, re_path
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('post', views.PostViewset, base_name='post')

app_name = 'posts'
urlpatterns =[
    path(r'crawl-username/', views.crawl_username, name='crawl_username'),
]

urlpatterns += router.urls
