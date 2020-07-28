from django.urls import path, include
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.postList.as_view(), name='home'),
    path('page/<int:page>', views.postList.as_view(), name='home'),
    path('api/', views.api, name='api'),
    path('article/<slug:slug>', views.postDetail.as_view(), name='post'),
    path('category/<slug:slug>', views.categoryList.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', views.categoryList.as_view(), name='category'),
]
