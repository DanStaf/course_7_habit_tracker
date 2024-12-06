from rest_framework.permissions import BasePermission


"""class IsModeratorClass(BasePermission):
    message = 'Moderators have access to all courses and lessons, but not allowed to delete and create'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()
"""


class IsOwnerClass(BasePermission):
    """
    Owners can update and delete personal habits
    All can view public habits
    """

    message = 'Only owner can operate this habit'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
