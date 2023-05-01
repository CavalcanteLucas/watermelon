from django.shortcuts import render
from formtools.wizard.views import CookieWizardView, SessionWizardView
from .forms import CustomerStoreNameForm, CustomerInfoForm, CustomerTypeForm


class customerFormSubmission(CookieWizardView):
    template_name = "datacollector/forms.html"
    form_list = [CustomerStoreNameForm, CustomerTypeForm, CustomerInfoForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, 'datacollector/home.html', {'form_data': form_data})