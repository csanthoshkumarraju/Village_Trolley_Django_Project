from django import forms

# class ShopSearchForm(forms.Form):
#     village_name = forms.CharField(max_length=1500, required=False, label='Village Name')

class Customer_ShopSearchForm(forms.Form):
    village_name = forms.CharField(
        max_length=1500, 
        required=False, 
        label='Village Name', 
        widget=forms.TextInput(attrs={
            'class': 'form-input', 
            'placeholder': 'Search village name'
        })
    )
