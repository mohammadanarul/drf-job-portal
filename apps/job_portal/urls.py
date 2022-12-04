from django.urls import path

from apps.job_portal import views

urlpatterns = [path("jobs/", views.JobPortalListCreateView.as_view())]
