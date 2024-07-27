from django import forms
from customer_registration_app.models import customer_registration_model

class customer_login_form(forms.Form):
    customer_phone_number = forms.CharField(max_length=10, required=True)
    customer_password = forms.CharField(max_length=10, widget=forms.PasswordInput, required=True)

    def clean_customer_phone_number(self):
        phone_number = self.cleaned_data.get('customer_phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("customer_phone_number")
        password = cleaned_data.get("customer_password")

        if phone_number and password:
            try:
                customer = customer_registration_model.objects.get(customer_phone_number=phone_number)
                if customer.customer_password != password:
                    raise forms.ValidationError("Incorrect password")
            except customer_registration_model.DoesNotExist:
                raise forms.ValidationError("Customer with this phone number does not exist")

        return cleaned_data