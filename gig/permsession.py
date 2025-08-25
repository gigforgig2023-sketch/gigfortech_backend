from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    message = 'Only clients can perform this action.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'client')


class IsFreelancer(BasePermission):
    message = 'Only freelancers can perform this action.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'freelancer')
