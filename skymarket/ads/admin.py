
# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

from django.contrib import admin

from skymarket.ads.models import Comment, Ad


admin.site.register(Ad)
admin.site.register(Comment)