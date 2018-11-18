from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        # is it a safe method (GET)?
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # it's not a safe method, so we check if it's their own profile
        # return the comparison (if it's the current user, return True, otherwise False)
        return obj.id == request.user.id