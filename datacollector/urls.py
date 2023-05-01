from django.urls import path
from .views import CustomerFormSubmission, CustomerInfoListView, customerFormSubmissionDoneView

app_name = "datacollector"

urlpatterns = [
    path("form/", CustomerFormSubmission.as_view(), name="customerformsubmission"),
    path("form/done/", customerFormSubmissionDoneView, name="customerformsubmission_done"),
    path("result/", CustomerInfoListView.as_view(), name="customerinfo_list"),
]
