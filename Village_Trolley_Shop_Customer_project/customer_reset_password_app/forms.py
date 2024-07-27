from django import forms
from customer_registration_app.models import customer_registration_model

class PasswordUpdateForm(forms.Form):
    mobile_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'styled-input',
            'placeholder': 'Please enter your registered mobile number.',
            'required': True
        })
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'styled-input',
            'placeholder': 'Please enter your new password here',
            'required': True
        })
    )
    confirm_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'styled-input',
            'placeholder': 'Please enter your new password here to confirm.',
            'required': True
        })
    )

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data['mobile_number']
        # Implement your validation logic for the mobile number here (e.g., length, digits only, etc.)
        if not mobile_number.isdigit() or len(mobile_number) != 10:
            raise forms.ValidationError("Invalid mobile number.")
        return mobile_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
