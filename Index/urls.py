from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_index, name="index"),
    path('store_index', views.store_index, name="store_index"),
    path('filter_category/<int:category_id>/', views.filter_products, name='filter_category'),
    path('products', views.view_all_products, name="products"),
    path('filter_products/<int:category_id>/', views.filter_products_all, name='filter_products'),
    path('subcategory_products/<str:subcategory>/', views.filter_products_subcategory, name='subcategory_products'),
    path('product_details/<int:product_id>/', views.product_detail, name='product_details'),
    path('ajax/check_stock/<str:product_name>/<str:product_subcategory>/<str:product_child_category>/'
         '<str:product_gender>/<str:product_brand>/<str:product_color>/', views.check_stock, name='ajax_check_stock'),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('store_login', views.login_store, name="store_login"),
    # path('home', views.home, name='home'),
    # path('logout', views.logout, name="logout"),

]