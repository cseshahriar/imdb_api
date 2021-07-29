from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    message = 'Allowed access to only admin users.'

    def has_permission(self, request, view):
        return  request.method == 'GET' or bool(request.user and request.user.is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):
    message = 'Allowed access to only review owner.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.user == request.user 