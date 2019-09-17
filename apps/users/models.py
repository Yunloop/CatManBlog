from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户模型类
    """
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=1, choices=(('0', "男"), ('1', "女")), null=True, verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    update_time = models.DateTimeField(null=True, blank=True, verbose_name="更新时间")
    last_login_time = models.DateTimeField(null=True, blank=True, verbose_name="最近登录时间")

    def __str__(self):
        return self.username
