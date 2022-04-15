from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from SportsStoreApp.views import count_cart_products


""" Main Index Page(First Page)"""


def main_index(request):
    return render(request, "main_index.html")


""" Sports Store Index page """


def store_index(request):
    category_all = categories.objects.all()[:12]
    # products = ProductDetails.objects.order_by().values_list('childcategory',flat=True).distinct()
    # products = ProductsDetails.objects.all().distinct('childcategory')[:9]
    products = ProductsDetails.objects.order_by('-childcategory').distinct('childcategory')[:9]
    return render(request, "store_index.html", {'categories': category_all, 'products': products})


def filter_products(request, category_id):
    category_all = categories.objects.all()[:12]
    products = ProductsDetails.objects.filter(childcategory=category_id)
    return render(request, "store_index.html", {'categories': category_all, 'products': products})


"""VIEW ALL PRODUCTS"""


def view_all_products(request):
    category_all = categories.objects.all()
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    # product = ProductsDetails.objects.order_by('-childcategory').distinct('childcategory', 'product_name')
    products = ProductsDetails.objects.order_by('-childcategory').distinct('childcategory', 'product_color')
    return render(request, "store_indexProductsAll.html",
                  {'categories': category_all, 'products': products, 'subcategories': sub_categories})


""" VIEWING ALL FILTERED PRODUCTS IN PRODUCTS PAGE """


def filter_products_all(request, category_id):
    category_all = categories.objects.all()
    products = ProductsDetails.objects.filter(childcategory=category_id)
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'),{'categories': category_all, 'products': products})
    return render(request, "store_indexProductsAll.html",
                  {'categories': category_all, 'products': products, 'subcategories': sub_categories})


"""VIEW PRODUCTS BASED ON SUBCATEGORY(SUBMENU IN PRODUCTS)"""


def filter_products_subcategory(request, subcategory):
    category_all = categories.objects.all()
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    # products = ProductsDetails.objects.filter(subcategory=subcategory).distinct('product_name')
    products = ProductsDetails.objects.filter(subcategory=subcategory)
    return render(request, "store_indexProductsAll.html",
                  {'categories': category_all, 'products': products, 'subcategories': sub_categories})


"""VIEW SINGLE  PRODUCT DETAILS """


def product_detail(request, product_id):
    print("......index/view product details")
    cart_count = count_cart_products(request)
    category_all = categories.objects.all()
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    product = ProductsDetails.objects.get(id=product_id)
    if product.product_size is not None:
        size_list = ProductsDetails.objects.filter(product_name=product.product_name, subcategory=product.subcategory,
                                                   childcategory=product.childcategory,
                                                   product_gender_for=product.product_gender_for).values_list(
            'product_size', flat=True).distinct()
    related_products = ProductsDetails.objects.filter(
        childcategory=product.childcategory) & ProductsDetails.objects.exclude \
                           (id=product_id) & ProductsDetails.objects.exclude(product_color=product.product_color)
    related_products = related_products.order_by('product_color', 'subcategory').distinct('product_color')
    return render(request, "store_indexProductDetail.html",
                  {'categories': category_all, 'subcategories': sub_categories, 'product': product,
                   'size_list': size_list, 'relatedProducts': related_products})


"""CHECKING STOCK WHILE SELECTING SIZE"""


def check_stock(request, product_name, product_subcategory, product_child_category, product_gender, product_brand,
                product_color):
    size_value = request.GET.get('size_value')
    child_category = categories.objects.get(subcategory=product_subcategory, childcategory=product_child_category)
    if ProductsDetails.objects.filter(product_size=size_value, product_name=product_name,
                                      subcategory=product_subcategory, childcategory=child_category.id,
                                      product_gender_for=product_gender, product_color=product_color,
                                      product_brand=product_brand).exists():
        product = ProductsDetails.objects.get(product_size=size_value, product_name=product_name,
                                              subcategory=product_subcategory, childcategory=child_category.id,
                                              product_gender_for=product_gender, product_color=product_color,
                                              product_brand=product_brand)

        productId = product.id
        stock = product.product_stock, productId
        print("............index/view check stock..........")
        product_detail(request, productId)
    else:
        stock = 'No such Products'
    return JsonResponse(stock, safe=False)


"""MAIN INDEX LOGIN CODE"""


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['userid'] = user.id
            return redirect('store/main_homepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'main_index_login.html')


"""MAIN INDEX REGISTER CODE"""


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email id is Already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password2, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                messages.success(request, 'Account Created Successfully!!! Login to explore ')
                return redirect('login')

        else:
            messages.info(request, 'Password is not matching')
            return redirect('register')
    else:
        return render(request, 'main_index_registerationpage.html')


"""LOG IN CODE FOR SPORTS STORE ALONG"""


def login_store(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['userid'] = user.id
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return redirect('store/store_homepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login_store')
    else:
        return render(request, 'store_LoginPage.html')
