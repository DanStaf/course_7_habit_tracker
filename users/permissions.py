from rest_framework.permissions import BasePermission


"""class IsModeratorClass(BasePermission):
    message = 'Moderators have access to all courses and lessons, but not allowed to delete and create'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()
"""


class IsOwnerClass(BasePermission):
    """
    all can view public habits
    Owners can update and delete public habits
    Owners can view, update and delete personal habits
    """

    message = 'Only owner can operate this habit'

    def has_object_permission(self, request, view, obj):
        # ??? to check
        return request.user == obj.owner
