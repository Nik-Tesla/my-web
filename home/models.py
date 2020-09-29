from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_converter, persian_number_converter
# from django.contrib.auth.models import User
from account.models import User

# My Manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='P')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True,
                               on_delete=models.SET_NULL, related_name='children', verbose_name='زیر دسته')
    tittle = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField("پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["parent__id", "position"]

    def __str__(self):
        return self.tittle

    objects = CategoryManager()


class homedb(models.Model):
    status_choices = (
        ('D', 'پیش نویس'),
        ('P', 'منتشر شده')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='article', verbose_name='نویسنده')
    tittle = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='article')
    document = models.TextField(verbose_name="محتوا")
    photo = models.ImageField(upload_to='images', verbose_name="تصویره مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان بروزرسانی")
    status = models.CharField(max_length=1, choices=status_choices, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.tittle+"    "+self.status

    def jpublish(self):
        return persian_number_converter(jalali_converter(self.publish))
    jpublish.short_description = "زمان انتشار"

    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description = "زمان ساخت"

    def jupdated(self):
        return jalali_converter(self.updated)
    jupdated.short_description = "بروزرسانی"

    def get_absolute_url(self):
        return reverse("account:home")
    # def category_published(self):
    #     return self.category.filter(status=True)

    def photo_tag(self):
        return format_html("<img height=70 width=110 style='border-radius: 5px;' src= '{}' >".format(self.photo.url))
    photo_tag.short_description = "تصویر مقاله "

    def category_to_str(self):
        return " , ".join([category.tittle for category in self .category.active()])
    category_to_str.short_description = "دسته بندی"

    objects = ArticleManager()
