from rest_framework.permissions import BasePermission


class IsUpdatable(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.user.id == user.id


class IsDestroyable(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.user.id == user.id
