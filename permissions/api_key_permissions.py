from rest_framework import permissions
from config.settings import API_SECRET


class APIKeyPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs. todo
    """

    def has_permission(self, request, view):
        return 'Secret' in request.headers and \
               request.headers['Secret'] == API_SECRET
        # if  and
        # secret = request.META['REMOTE_ADDR']
        # blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        # return not blacklisted
