from django.contrib import admin

from apps.job_portal.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "vacancy",
        "address",
        "sellery",
        "expiry_date",
        "description",
        "expiry",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "user",
        "expiry_date",
        "expiry",
        "created_at",
        "updated_at",
    )
    raw_id_fields = ("skils", "employees")
    date_hierarchy = "created_at"
