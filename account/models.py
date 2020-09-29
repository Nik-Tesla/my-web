from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
	is_author = models.BooleanField(default=False,verbose_name='وضعیت نویسندگی')
	spcial_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

	def is_spcial_user(self):
		if self.spcial_user > timezone.now():
			return True
		else:
			return False
	is_spcial_user.boolean = True
	is_spcial_user.short_description = "کاربر ویژه"