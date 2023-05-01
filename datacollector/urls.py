from django.urls import path
from .views import customerFormSubmission

app_name = "datacollector"

urlpatterns = [
    path("", customerFormSubmission.as_view(), name="application"),
]
