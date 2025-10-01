from django.forms import ModelForm
from main.models import Product, Seller
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "description", "price", "category", "image", "in_stock"]
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'w-full border-green-900 rounded-md shadow-sm'}),
            'description': forms.Textarea(attrs={'class': 'w-full border-green-300 rounded-md shadow-sm', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'w-full border-green-300 rounded-md shadow-sm'}),
            'category': forms.Select(attrs={'class': 'w-full border-green-300 rounded-md shadow-sm'}),
            'image': forms.URLInput(attrs={'class': 'w-full border-green-300 rounded-md shadow-sm'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-green-600 border-green-300 rounded'}),
        }
        

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ["seller_name", "email_seller"]
