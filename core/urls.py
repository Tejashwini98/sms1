from django.urls import path
from . import views

app_name="core"
urlpatterns = [
    path("", views.application_view, name="apply_schoolarship"),
    path("approval/", views.approval_view, name="approval"),
    path("amount/", views.amount_view, name="amount"),

    path("applications/", views.no_of_application, name="applications"),
    path("applications-details/<int:pk>/", views.applicant_detail, name="applications_detail"),

    path("approved-applications/", views.approved_application_view, name="approved_applications"),
    path("rejected-applications/", views.rejected_application_view, name="rejected_applications"),
    path("pending-applications/", views.pending_application_view, name="pending_applications"),
    path("applications-status/<int:pk>/", views.application_status_view, name="applications_status"),
    path("applications-reject/<int:pk>/", views.reject_view, name="application_reject"),
    path("applications-approve/<int:pk>/", views.approve_view, name="application_approve"),
    path("applications-processing/<int:pk>/", views.processing_view, name="applications_processing"),

    path("create-scheme/", views.create_scheme_view, name="create_scheme"),
]