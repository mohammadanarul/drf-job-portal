from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class EmployeePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Employee").exists():
            return True


class RecruiterPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Recruiter").exists():
            return True
