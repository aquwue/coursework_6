import datetime

from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

from skymarket.users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    price = models.PositiveIntegerField(validators=[MinLengthValidator(0)])
    description = models.TextField(max_length=1000, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(datetime.datetime)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ManyToManyField(Ad)
    created_at = models.DateTimeField(datetime.datetime)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name
