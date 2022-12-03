from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from apps.users.views import auth_views, employee_views, recruiter_views

urlpatterns = [
    # jwt token api
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # employee urls
    path("employees/", employee_views.EmployeeListView.as_view(), name="employees"),
    path(
        "employees/<pk>/",
        employee_views.EmployeeRetrieveUpdateDestroyAPIView.as_view(),
    ),
    # recruiter urls
    path("recruiters/", recruiter_views.RecruiterListView.as_view()),
    path(
        "recruiters/<pk>/",
        recruiter_views.RecruiterRetrieveUpdateDestroyAPIView.as_view(),
    ),
    # auth urls
    path("otp/verify/", auth_views.OTPVerify.as_view(), name="otp_verify"),
]
