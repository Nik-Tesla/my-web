from django.urls import path, include
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('page/<int:page>', views.home, name='home'),
    path('api/', views.api, name='api'),
    path('article/<slug:slug>', views.post, name='post'),
    path('category/<slug:slug>', views.category, name='category'),
    path('category/<slug:slug>/page/<int:page>', views.category, name='category'),
]
