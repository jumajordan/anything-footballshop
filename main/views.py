import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.forms import ProductForm, SellerForm
from main.models import Product, Seller
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    category = request.GET.get("category")

    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    if category:
        product_list = product_list.filter(category=category)

    seller_list = Seller.objects.all()
    context = {
        'first': 'What Do You Want to Buy?',
        'shop': 'Enter the shop',
        'desc': 'In this shop you will find everything about football',
        'aboutme': 'Juma Jordan Bimo, 2406435843',
        'product_list': product_list,
        'seller_list': seller_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'CATEGORY_CHOICES': Product.CATEGORY_CHOICES,
    }
    return render(request, "main.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    price = request.POST.get("price")
    image = request.POST.get("image")
    in_stock = request.POST.get("in_stock") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        product_name=product_name,
        description=description,
        category=category,
        price=price,
        image=image,
        in_stock=in_stock,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

def create_seller(request):
    form = SellerForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_seller.html", context)

def show_seller_xml(request):
    seller_list = Seller.objects.all()
    xml_data = serializers.serialize("xml", seller_list)
    return HttpResponse(xml_data, content="application/xml")

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    try:
        product_list = Product.objects.all()
        data = [
            {
                'id': str(product.id),
                'product_name': product.product_name,
                'description': product.description,
                'category': product.category,
                'image': product.image,
                'product_views': product.product_views,
                'created_at': product.created_at.isoformat() if product.created_at else None,
                'in_stock': product.in_stock,
                'price': str(product.price),
                'user_id': product.user,
            }
            for product in product_list
        ]
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
            return JsonResponse({'detail': 'Not found'}, status=404)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)

        data = {
            "id": str(product.id),
            "product_name": product.product_name,
            "description": product.description,
            "category": product.category,
            "image": product.image,
            "product_views": product.product_views,
            "created_at": product.created_at.isoformat() if product.created_at else None,
            "in_stock": product.in_stock,
            "is_product_trend": product.is_product_trend,
            "price": float(product.price),
            "user_username": product.user.username if product.user else None
        }

        return JsonResponse(data)

    except Product.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)