from django.urls import path
# Tambahkan import untuk view mobile baru
from main.views import (
    show_main, create_product, show_product, show_xml, show_json, 
    show_xml_by_id, show_json_by_id, create_seller, 
    login_user, register, logout_user, edit_product, delete_product, 
    add_product_entry_ajax,
    # Import fungsi baru di sini:
    login_mobile, logout_mobile, register_mobile 
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('createseller/', create_seller, name="create_seller"),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('add-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('auth/login/', login_mobile, name='login_mobile'),
    path('auth/register/', register_mobile, name='register_mobile'),
    path('auth/logout/', logout_mobile, name='logout_mobile'),
    
]