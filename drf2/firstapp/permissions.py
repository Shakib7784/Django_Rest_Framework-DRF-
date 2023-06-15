from rest_framework import permissions


class AdminorReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #safe method is giving only read access
            return True
        else : #giving read,write access
            bool(request.user and request.user.is_staff) # if user is authenticated and stafff
            
            
                    
class ReviewerOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else : 
            return obj.user ==request.user # if user is match with requested user. obj.user means user in database