from django.urls import path, include
from . import views

urlpatterns = [
    path('main_homepage', views.main_homepage, name="main_homepage"),
    path('store_homepage', views.store_homepage, name="store_homepage"),
    path('filter_category_products/<int:category_id>/', views.category_products, name='filter_category_products'),
    path('products_all', views.view_all_products, name="products_all"),
    path('filterCategory_productsAll/<int:category_id>/', views.category_products_all,
         name='filterCategory_productsAll'),
    path('subcategory_productsAll/<str:subcategory>/', views.subcategory_products, name='subcategory_productsAll'),
    path('productDetails/<int:product_id>/', views.product_details, name='productDetails'),
    path('ajax/add_ToCart/', views.add_ToCart, name='ajax_add_ToCart'),
    path('login_redirect', views.login_redirect, name="login_redirect"),
    path('show_cart', views.show_cart, name="show_cart"),
    path('update_quantity', views.update_quantity, name="update_quantity"),
    path('remove_product/<int:product_id>/<int:cart_id>/', views.remove_cart_product, name='remove_product'),
    path('show_wishlist', views.show_wishlist, name="show_wishlist"),
    path('add-remove-wishlist', views.add_remove_wishlist, name="add-remove-wishlist"),
    path('add-ToCart', views.add_ToCart, name='add-ToCart'),
    path('checkout', views.checkout, name='checkout'),
    path('booking_product',views.booking_products,name='booking_product'),
    path('logout', views.logout, name="logout"),
]
