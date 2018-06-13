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

class PostOwnStatus(permissions.BasePermission):
    '''
    Allow users to update their own statusself.
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Checks if the user is trying to update its own status.
        '''
        if request.method in permissions.SAFE_METHODS:

            return True

        return obj.user_profile.id == request.user.id
