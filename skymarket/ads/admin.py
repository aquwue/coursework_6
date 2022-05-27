
# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

from django.contrib import admin

from skymarket.ads.models import Comment, Ad
from skymarket.users.models import User

admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Ad)
