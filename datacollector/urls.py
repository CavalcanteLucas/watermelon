from django.urls import path
from .views import customerFormSubmission
from .forms import CustomerInfoForm, CustomerTypeForm


app_name = "datacollector"
form_list = [CustomerTypeForm, CustomerInfoForm]

urlpatterns = [
    path("", customerFormSubmission.as_view(), name="application"),
]
