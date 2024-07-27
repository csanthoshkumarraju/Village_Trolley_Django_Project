from django import forms
from .models import customer_registration_model

class customer_registartion_form(forms.ModelForm):
    class Meta:
        model = customer_registration_model
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['customer_first_name'].widget.attrs.update({
                'placeholder': 'Enter Your first name'
            })
        self.fields['customer_last_name'].widget.attrs.update({
                'placeholder': 'Enter Your last name'
            })
        self.fields['customer_mail_id'].widget.attrs.update({
                'placeholder': 'Enter Your mail ID'
            })
        self.fields['customer_phone_number'].widget.attrs.update({
                'placeholder': 'Enter Your 10 digit phone number'
            })
        self.fields['customer_password'].widget = forms.PasswordInput()
        self.fields['customer_password'].widget.attrs.update({
                'placeholder': 'Enter Your Password'
            })
        self.fields['customer_confirm_password'].widget = forms.PasswordInput()
        self.fields['customer_confirm_password'].widget.attrs.update({
                'placeholder': 'Enter Your password again to confirm'
            })
        
    def clean(self):
        cleaned_data = super().clean()
        customer_password = cleaned_data.get("customer_password")
        customer_confirm_password = cleaned_data.get("customer_confirm_password")

        if customer_password and customer_confirm_password and customer_password != customer_confirm_password:
            self.add_error('customer_confirm_password', "Passwords do not match.")
        return cleaned_data
        
    def save(self, commit=True):
    # Override save method if needed
        return super().save(commit=commit)





     
