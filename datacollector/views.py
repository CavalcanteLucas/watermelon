from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from .forms import (
    CustomerStoreNameForm,
    CustomerBalanceLeftForm,
    CustomerSellPriceForm,
    CustomerTargetNetworkForm,
    CustomerTargetAddressForm,
    CustomerClientAddressForm,
)


class customerFormSubmission(SessionWizardView):
    template_name = "datacollector/forms.html"
    form_list = [
        CustomerStoreNameForm,
        CustomerBalanceLeftForm,
        CustomerSellPriceForm,
        CustomerTargetNetworkForm,
        CustomerTargetAddressForm,
        CustomerClientAddressForm,
    ]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, "datacollector/done.html", {"form_data": form_data})
