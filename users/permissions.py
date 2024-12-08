from rest_framework.permissions import BasePermission


class IsOwnerClass(BasePermission):
    """
    Owners can update and delete personal habits
    All can view public habits
    """

    message = 'Only owner can operate this habit'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
