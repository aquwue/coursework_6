# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions
from skymarket.ads.models import Comment, Ad
from skymarket.users.models import User
from django.http import Http404


class CommentOwner(permissions.BasePermission):
    message = 'Managing others selections not permitted.'

    def has_permission(self, request, view):
        try:
            entity = Comment.objects.get(pk=view.kwargs["pk"])
        except Comment.DoesNotExist:
            raise Http404

        if entity.owner_id == request.user.id:
            return True
        return False


class AdOwner(permissions.BasePermission):
    message = 'Managing others selections not permitted.'

    def has_permission(self, request, view):
        if request.user.role in [User.MEMBER, User.ADMIN]:
            return True

        try:
            entity = Ad.objects.get(pk=view.kwargs["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if entity.owner_id == request.user.id:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    message = 'You are not administrator.'

    def has_permission(self, request, view):
        try:
            entity = request.user.get(pk=view.kwargs["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if request.user.role == User.ADMIN:
            return True
        return False
