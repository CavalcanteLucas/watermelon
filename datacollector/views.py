from django.shortcuts import render, redirect
from django.views import generic
from formtools.wizard.views import SessionWizardView
from .forms import (
    CustomerStoreNameForm,
    CustomerBalanceLeftForm,
    CustomerSellPriceForm,
    CustomerTargetNetworkForm,
    CustomerTargetAddressForm,
    CustomerClientAddressForm,
)
from .models import CustomerInfo
from django.http import HttpResponseRedirect


class CustomerFormSubmission(SessionWizardView):
    template_name = "datacollector/forms.html"
    form_list = [
        CustomerStoreNameForm,
        CustomerBalanceLeftForm,
        CustomerSellPriceForm,
        CustomerTargetNetworkForm,
        CustomerTargetAddressForm,
        CustomerClientAddressForm,
    ]

    def get_form_initial(self, step):
        initial = self.storage.get_step_data(step)
        if initial:
            return self.storage.get_step_data(step)
        return self.initial_dict.get(step, {})

    def done(self, form_list, **kwargs):
        customer_info = CustomerInfo()
        for form in form_list:
            customer_info.__dict__.update(form.cleaned_data)
        customer_info.save()
        self.storage.reset()
        return HttpResponseRedirect("done/")


class CustomerInfoListView(generic.ListView):
    model = CustomerInfo

def customerFormSubmissionDoneView(request):
    return render(request, "datacollector/done.html")

def indexView(request):
    return redirect("datacollector:customerformsubmission")