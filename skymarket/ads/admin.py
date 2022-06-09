
# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

from django.contrib import admin

from skymarket.ads.models import Comment, Ad


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("pk", "author", "text")


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = ("pk", "author", "title", "price", "image")
