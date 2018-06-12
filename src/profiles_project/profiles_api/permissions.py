from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''
    Allow users to edit their own profile.
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Checks if user is trying to edit its own profile.
        '''
        if request.method in permissions.SAFE_METHODS:

            return True

        return obj.id == request.user.id