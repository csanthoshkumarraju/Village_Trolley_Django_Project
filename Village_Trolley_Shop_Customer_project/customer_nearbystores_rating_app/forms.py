from django import forms
from .models import shop_owner_registration_model, Rating

# class ShopAndRatingForm(forms.ModelForm):
#     shop_name = forms.CharField(
#         label='Search Shop',
#         max_length=250,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter shop name',
#             'class': 'form-control'
#         })
#     )
    
#     class Meta:
#         model = Rating
#         fields = ['rating']
#         widgets = {
#             'rating': forms.NumberInput(attrs={
#                 'min': 1,
#                 'max': 5,
#                 'placeholder': 'Rate from 1 to 5',
#                 'class': 'form-control'
#             })
#         }
#         labels = {
#             'rating': 'Rating'
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         shop_name = cleaned_data.get('shop_name')
        
#         if shop_name:
#             try:
#                 shop = shop_owner_registration_model.objects.get(shop_owner_shop_name__iexact=shop_name)
#                 cleaned_data['shop'] = shop
#             except shop_owner_registration_model.DoesNotExist:
#                 raise forms.ValidationError("Shop not found.")
#         return cleaned_data


class ShopSearchForm(forms.Form):
    shop_name = forms.CharField(
        label='Search Shop',
        max_length=250,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter shop name',
            'class': 'form-control'
        })
    )

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'placeholder': 'Rate from 1 to 5',
                'class': 'form-control'
            })
        }
        labels = {
            'rating': 'Rating'
        }