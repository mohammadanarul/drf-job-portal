from django.contrib import admin

from apps.profiles.models import EmployeeProfile, RecruiterProfile


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "company_name",
        "website_url",
        "country",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at", "user")
    date_hierarchy = "created_at"


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "cv_pdf",
        "bio",
        "country",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at", "user", "date_of_birth")
    raw_id_fields = ("skils",)
    date_hierarchy = "created_at"
