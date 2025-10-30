from django.forms import ModelForm
from main.models import Product, Seller
from django import forms
from django.utils.html import strip_tags

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
    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
        

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ["seller_name", "email_seller"]
