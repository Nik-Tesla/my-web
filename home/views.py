from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import homedb, Category
# Create your views here.


def home(request, page=1):
    posts_list = homedb.objects.published()
    paginator = Paginator(posts_list, 4)
    posts = paginator.get_page(page)
    context = {
        "posts": posts,

    }
    return render(request, 'home/home.html', context)


def post(request, slug):
    context = {"post": get_object_or_404(homedb.objects.published(), slug=slug)}
    return render(request, 'home/post.html', context)


def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    posts_list = category.article.published()
    paginator = Paginator(posts_list, 4)
    posts = paginator.get_page(page)
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, 'home/category.html', context)


def api(request):
    data = {
        '0': {
            'name': 'ali0',
            'id': 0,
            'phone': 0},
        '1': {
            'name': 'ali1',
            'id': 1,
            'phone': 1},
        '2': {
            'name': 'ali2',
            'id': 2,
            'phone': 2},
        '3': {
            'name': 'ali3',
            'id': 3,
            'phone': 3}
    }

    return JsonResponse(data)
