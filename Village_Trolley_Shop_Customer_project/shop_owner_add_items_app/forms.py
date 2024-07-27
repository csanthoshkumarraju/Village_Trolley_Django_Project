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

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        buying_price = cleaned_data.get('product_buying_price')
        selling_price = cleaned_data.get('product_selling_price')
        quantity = cleaned_data.get('product_qunatity')
        storage_place = cleaned_data.get('product_storage_place')

        # Validate that all fields are filled out
        if not product_name:
            self.add_error('product_name', 'Product name is required.')
        if not buying_price:
            self.add_error('product_buying_price', 'Buying price is required.')
        if not selling_price:
            self.add_error('product_selling_price', 'Selling price is required.')
        if not quantity:
            self.add_error('product_qunatity', 'Quantity is required.')
        if not storage_place:
            self.add_error('product_storage_place', 'Storage place is required.')
        
        return cleaned_data