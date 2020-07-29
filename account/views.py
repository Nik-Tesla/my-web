from django.shortcuts import render
##from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from home.models import homedb
# Create your views here.


# @login_required
# def home(request):
# return render(request, 'registration/home.html')


class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return homedb.objects.all()
        else:
            return homedb.objects.filter(author=self.request.user)


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = homedb
    fields = ["author", "tittle", "slug", "category", "document", "photo", "publish", "status"]
    template_name = 'registration/article-create-update.html'
