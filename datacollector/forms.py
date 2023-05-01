from django import forms


class CustomerStoreNameForm(forms.Form):
    store_name = forms.CharField(
        label="Store Name",
        max_length=200,
        required=False,
    )


class CustomerBalanceLeftForm(forms.Form):
    balance_left = forms.IntegerField(
        label="Balance Left",
        required=False,
    )


class CustomerSellPriceForm(forms.Form):
    selling_price = forms.IntegerField(
        label="Selling Price",
        required=False,
    )


class CustomerTargetNetworkForm(forms.Form):
    TARGET_NETWORK_CHOICES = [
        ("polygon", "Polygon"),
        ("etherium", "Etherium"),
    ]

    target_network = forms.CharField(
        label="Target Network",
        widget=forms.RadioSelect(choices=TARGET_NETWORK_CHOICES),
        required=False,
    )


class CustomerTargetAddressForm(forms.Form):
    target_address = forms.CharField(
        label="Target Address",
        max_length=200,
        required=False,
    )


class CustomerClientAddressForm(forms.Form):
    client_email = forms.EmailField(
        label="Client Email",
        max_length=200,
        required=False,
    )
