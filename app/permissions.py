__author__ = 'stikks'

from rest_framework import permissions

from .models import TransportationProvider


class IsOwnerorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsProviderOwnerorReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        print 'view', view
        print 'request', request
        print 'obj', obj

        return False