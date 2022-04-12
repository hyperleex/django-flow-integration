from django.urls import path

from accounts import views

urlpatterns = [
    path("accounts/", views.AccountList.as_view(), name="account-list"),
    path("accounts/<str:address>/", views.get_account, name="account-detail"),
    path("job_status/", views.update_job, name="job-status"),
]
