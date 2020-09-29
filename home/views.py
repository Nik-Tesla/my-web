from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import homedb, Category
from django.views.generic import ListView, DetailView
from account.models import User

# Create your views here.


# def home(request, page=1):
#     posts_list = homedb.objects.published()
#     paginator = Paginator(posts_list, 4)
#     posts = paginator.get_page(page)
#     context = {
#         "posts": posts,

#     }
#     return render(request, 'home/home.html', context)

class postList(ListView):
    #model = homedb
    #template_name = "home/home.html"
    #context_object_name = "posts"
    queryset = homedb.objects.published()
    paginate_by = 4

# def post(request, slug):
#     context = {"post": get_object_or_404(homedb.objects.published(), slug=slug)}
#     return render(request, 'home/post.html', context)


class postDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(homedb.objects.published(), slug=slug)


# def category(request, slug, page=1):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     posts_list = category.article.published()
#     paginator = Paginator(posts_list, 4)
#     posts = paginator.get_page(page)
#     context = {
#         "category": category,
#         "posts": posts
#     }
#     return render(request, 'home/category.html', context)

class categoryList(ListView):
    paginate_by = 4
    template_name = "home/categoryList.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.article.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    paginate_by = 4
    template_name = "home/author_List.html"

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.article.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context


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
