from rest_framework import permissions

from config.settings import API_SECRET


class APIKeyPermission(permissions.BasePermission):
    """Check if there is correct secret api key in request header"""

    def has_permission(self, request, view):
        return 'Secret' in request.headers and \
               request.headers['Secret'] == API_SECRET
