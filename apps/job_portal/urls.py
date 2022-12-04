from django.urls import path

from apps.job_portal import views

urlpatterns = [
    path("", views.JobPortalListCreateView.as_view()),
    path("<pk>/", views.JobPortalRetrieveUpdateDestroyAPI.as_view()),
]
