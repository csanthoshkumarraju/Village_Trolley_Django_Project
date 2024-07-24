from django import forms
from .models import shop_owner_registration_model

class shop_owner_registration_form(forms.ModelForm):
    class Meta:
        model = shop_owner_registration_model
        fields = '__all__'
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['shop_owner_first_name'].widget.attrs.update({
            'placeholder': 'Enter Your first name'
        })
        self.fields['shop_owner_last_name'].widget.attrs.update({
            'placeholder': 'Enter Your last name'
        })

        self.fields['shop_owner_shop_name'].widget.attrs.update({
            'placeholder': 'Enter Your shop name'
        })

        self.fields['shop_owner_mail_id'].widget.attrs.update({
            'placeholder': 'Enter Your mail Id'
        })

        self.fields['shop_owner_phone_number'].widget.attrs.update({
            'placeholder': 'Enter Your 10 digit phone number'
        })
        
        self.fields['shop_owner_street_address'].widget.attrs.update({
            'placeholder': 'Enter Your street address'
        })

        self.fields['shop_owner_village_name'].widget.attrs.update({
            'placeholder': 'Enter Your village name'
        })

        self.fields['shop_owner_mandal_name'].widget.attrs.update({
            'placeholder': 'Enter Your mandal name'
        })

        self.fields['shop_owner_city_name'].widget.attrs.update({
            'placeholder': 'Enter Your city name'
        })

        self.fields['shop_owner_state_name'].widget.attrs.update({
            'placeholder': 'Enter Your state name'
        })

        self.fields['shop_owner_pincode'].widget.attrs.update({
            'placeholder': 'Enter Your area pin code'
        })
        self.fields['shop_owner_password'].widget = forms.PasswordInput()
        self.fields['shop_owner_password'].widget.attrs.update({
            'placeholder': 'Enter Your password'
        })
        self.fields['shop_owner_confirm_password'].widget = forms.PasswordInput()
        self.fields['shop_owner_confirm_password'].widget.attrs.update({
            'placeholder': 'Enter Your password again to confirm'
        })
    def clean(self):
        cleaned_data = super().clean()
        shop_owner_password = cleaned_data.get("shop_owner_password")
        shop_owner_confirm_password = cleaned_data.get("shop_owner_confirm_password")

        if shop_owner_password and shop_owner_confirm_password and shop_owner_password != shop_owner_confirm_password:
            self.add_error('shop_owner_confirm_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        # Override save method if needed
        return super().save(commit=commit)