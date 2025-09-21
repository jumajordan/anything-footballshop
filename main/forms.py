from django.forms import ModelForm
from main.models import Product, Seller

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "description", "price", "category", "image", "in_stock"]

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ["seller_name", "email_seller"]