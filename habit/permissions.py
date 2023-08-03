from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может изменять или удалять только свои привычки.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить только чтение для неавторизованных пользователей
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить изменение или удаление только владельцу привычки
        return obj.user == request.user


class IsAuthenticatedOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Разрешить доступ на чтение неавторизованным пользователям,
    но требовать авторизации для любых других действий.
    """
    pass
