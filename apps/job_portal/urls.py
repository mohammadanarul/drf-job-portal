from django.urls import path

from apps.job_portal.views import ApiView

urlpatterns = [path("", ApiView.as_view(), name="home")]
