from django import forms
from shop_owner_registration_app.models import shop_owner_registration_model

class shop_owner_login_form(forms.Form):
    phone_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        password = cleaned_data.get("password")
        
        if phone_number and password:
            try:
                shop_owner = shop_owner_registration_model.objects.get(shop_owner_phone_number=phone_number)
                if shop_owner.shop_owner_password != password:
                    raise forms.ValidationError("Incorrect password")
            except shop_owner_registration_model.DoesNotExist:
                raise forms.ValidationError("Shop owner with this phone number does not exist")
        
        return cleaned_data
