from django.urls import path, include
from .views import *

app_name = 'home'
urlpatterns = [
    path('', postList.as_view(), name='home'),
    path('page/<int:page>', postList.as_view(), name='home'),
    path('api/', api, name='api'),
    path('article/<slug:slug>', postDetail.as_view(), name='post'),
    path('category/<slug:slug>', categoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', categoryList.as_view(), name='category'),

    path('author/<slug:username>', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),
]
