# posts/permissions.py
from rest_framework.permissions import BasePermission
  
  
class IsAuthorOrReadOnly(BasePermission):
  
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
    
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user