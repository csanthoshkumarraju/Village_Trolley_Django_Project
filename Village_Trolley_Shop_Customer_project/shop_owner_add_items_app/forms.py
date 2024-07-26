from django import forms
from .models import shop_owner_add_items

class shop_owner_add_items_form(forms.ModelForm):
    class Meta:
        model = shop_owner_add_items
        fields = '__all__'
        exclude = ['shop_user_name']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['product_name'].widget.attrs.update({
            'placeholder': 'Enter product name'
        })
        self.fields['product_buying_price'].widget.attrs.update({
            'placeholder': 'Enter product buying price'
        })
        self.fields['product_selling_price'].widget.attrs.update({
            'placeholder': 'Enter product selling price'
        })
        self.fields['product_qunatity'].widget.attrs.update({
            'placeholder': 'Enter product quantity'
        })
        self.fields['product_storage_place'].widget.attrs.update({
            'placeholder': 'Enter product storage place'
        })