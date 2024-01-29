from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedForManipulation(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)
