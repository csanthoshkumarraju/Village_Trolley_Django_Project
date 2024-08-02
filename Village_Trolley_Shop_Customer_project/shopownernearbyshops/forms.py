from django import forms

class ShopSearchForm(forms.Form):
    village_name = forms.CharField(max_length=1500, required=False, label='Village Name')

      