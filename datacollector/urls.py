from django.urls import path
from django.shortcuts import redirect
from .views import (
    CustomerFormSubmission,
    CustomerInfoListView,
    customerFormSubmissionDoneView,
    indexView,
)

app_name = "datacollector"

urlpatterns = [
    path("form/", CustomerFormSubmission.as_view(), name="customerformsubmission"),
    path("form/done/", customerFormSubmissionDoneView, name="customerformsubmission_done"),
    path("results/", CustomerInfoListView.as_view(), name="customerinfo_list"),
    path("", indexView, name="index",)
]
