from rest_framework import permissions


# Custom permission to only allow owners of an object to edit it.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # GET, HEAD and OPTIONS requests are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user
