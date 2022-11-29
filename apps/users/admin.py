from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Employee, Recruiter, User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "phone_number",
        "email",
        "roll",
        "last_login",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "last_login",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    fieldsets = ()
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "email", "password1", "password2"),
            },
        ),
    )
    readonly_fields = ("pk", "date_joined", "last_login")
    filter_horizontal = []
    search_fields = ("phone_number", "email")
    ordering = ("phone_number",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "password",
        "last_login",
        "full_name",
        "phone_number",
        "email",
        "roll",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "last_login",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = (
        "password",
        "last_login",
        "full_name",
        "phone_number",
        "email",
        "roll",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "last_login",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
