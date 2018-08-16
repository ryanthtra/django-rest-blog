# posts/permissions.py
from rest_framework import permissions



# extends BasePermission
class IsAuthorOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    # Read-only permissions allowed for any request
    if request.method in permissions.SAFE_METHODS:
      # SAFE_METHODS are GET, OPTIONS, and HEAD
      return True

    # Write permissions allowed only for author
    return obj.author == request.user