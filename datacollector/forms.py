from django import forms


class CustomerStoreNameForm(forms.Form):
    store_name = forms.CharField(
        label="Store Name",
        max_length=200,
        required=True,
    )


class CustomerBalanceLeftForm(forms.Form):
    balance_left = forms.IntegerField(
        label="Balance Left",
        required=True,
    )


class CustomerSellPriceForm(forms.Form):
    selling_price = forms.IntegerField(
        label="Selling Price",
        required=True,
    )


class CustomerTargetNetworkForm(forms.Form):
    TARGET_NETWORK_CHOICES = [
        ("polygon", "Polygon"),
        ("etherium", "Etherium"),
    ]

    target_network = forms.CharField(
        label="Target Network",
        widget=forms.RadioSelect(choices=TARGET_NETWORK_CHOICES),
        required=True,
    )


class CustomerTargetAddressForm(forms.Form):
    target_address = forms.CharField(
        label="Target Address",
        max_length=200,
        required=True,
    )


class CustomerClientAddressForm(forms.Form):
    client_email = forms.EmailField(
        label="Client Email",
        max_length=200,
        required=True,
    )
