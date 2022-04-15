from django.shortcuts import render, redirect
from Index.models import *
from .models import CartTable, WishlistTable
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.
"""MAIN HOME PAGE"""


def main_homepage(request):
    userid = request.session['userid']
    user_details = User.objects.get(id=userid)
    return render(request, "main_homepage.html", {'user': user_details})


"""SPORTS STORE HOME PAGE"""


def store_homepage(request):
    userid = request.session['userid']
    user_details = User.objects.get(id=userid)
    category_all = categories.objects.all()[:12]
    products = ProductsDetails.objects.order_by('-childcategory').distinct('childcategory')[:9]
    cart_count = count_cart_products(request)
    return render(request, "store_homepage.html",
                  {'categories': category_all, 'products': products, 'user': user_details, 'cart_count': cart_count})


""" VIEW PRODUCTS BASED ON CATEGORIES LISTED IN THE LEFT SIDE """


def category_products(request, category_id):
    category_all = categories.objects.all()[:12]
    products = ProductsDetails.objects.filter(childcategory=category_id)
    cart_count = count_cart_products(request)
    return render(request, "store_homepage.html",
                  {'categories': category_all, 'products': products, 'cart_count': cart_count})


""" VIEW ALL PRODUCTS BASED ON CATEGORIES LISTED IN THE LEFT SIDE IN PRODUCTS PAGE """


def category_products_all(request, category_id):
    category_all = categories.objects.all()
    products = ProductsDetails.objects.filter(childcategory=category_id)
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    cart_count = count_cart_products(request)
    return render(request, "store_ProductsAll.html",
                  {'categories': category_all, 'products': products, 'subcategories': sub_categories,
                   'cart_count': cart_count})


"""VIEW ALL PRODUCTS WHILE CLICKING PRODUCTS"""


def view_all_products(request):
    category_all = categories.objects.all()
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    products = ProductsDetails.objects.order_by('-childcategory').distinct('childcategory', 'product_color')
    cart_count = count_cart_products(request)
    return render(request, "store_ProductsAll.html",
                  {'categories': category_all, 'products': products, 'subcategories': sub_categories,
                   'cart_count': cart_count})


"""VIEW ALL PRODUCTS BASED ON SUBCATEGORY(SUBMENU IN PRODUCTS)"""


def subcategory_products(request, subcategory):
    category_all = categories.objects.all()
    sub_categories = categories.objects.order_by('-subcategory').values_list('subcategory', flat=True).distinct()
    products = ProductsDetails.objects.filter(subcategory=subcategory)
    cart_count = count_cart_products(request)
    return render(request, "store_ProductsAll.html",
                  {'categories': category_all, 'products': products, 'subcategories': sub_categories,
                   'cart_count': cart_count})


"""VIEW SINGLE  PRODUCT DETAILS """


def product_details(request, product_id):
    wishlist_in = check_wishlist_icon(request, product_id)
    print(".....wishkist status.....",wishlist_in)
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
    cart_count = count_cart_products(request)
    return render(request, "store_ProductDetail.html",
                  {'categories': category_all, 'subcategories': sub_categories, 'product': product,
                   'size_list': size_list, 'relatedProducts': related_products, 'cart_count': cart_count,
                   'wishlist': wishlist_in})


""" ADD TO CART """


def add_ToCart(request):
    if 'userid' not in request.session:
        return JsonResponse({'status': "Login to continue"})
        # return redirect('login_redirect')
    else:
        userid = request.session['userid']
        cart_count = count_cart_products(request)
        if request.user.is_authenticated:
            print("......wishlist addtocart......")
            product_id = request.GET.get('product_id')
            if product_id is None:
                product_id = request.POST.get('product_id')
            product_check = ProductsDetails.objects.get(id=product_id)
            if product_check:
                user = User.objects.get(id=userid)
                if CartTable.objects.filter(product_id=product_check, user_id=userid).exists():
                    return JsonResponse({'status': "Product Already in cart"})
                else:
                    CartTable.objects.create(user_id=userid, product_id=product_check)
                    return JsonResponse({'status': "Product added successfully"})
            else:
                return JsonResponse({'status': "No such product"})
        else:
            return JsonResponse({'status': "Login to continue"})


""" VIEW CART PAGE"""


def show_cart(request):
    if 'userid' not in request.session:
        return redirect('login_redirect')
    else:
        userid = request.session['userid']
        cart_count = count_cart_products(request)
        if request.user.is_authenticated:
            products = CartTable.objects.filter(user_id=userid).order_by('-id')
            if products:
                total_amount = 0
                for item in products:
                    total_amount += item.total_price()
                return render(request, 'store_ShoppingCart.html',
                              {'products': products, 'total': total_amount, 'cart_count': cart_count})
            else:
                messages.info(request, 'No Products in the cart')
                return render(request, 'store_ShoppingCart.html')
        else:
            return redirect('login_redirect')


"""UPDATE QUANTITY"""


def update_quantity(request):
    if 'userid' not in request.session:
        return JsonResponse({'status': "Login to continue"})
    else:
        userid = request.session['userid']
        cart_count = count_cart_products(request)
        if request.user.is_authenticated:
            product_id = request.GET.get('product_id')
            quantity = request.GET.get('quantity')
            product_det = ProductsDetails.objects.get(id=product_id)
            if product_det and int(quantity) in range(1, 11):
                product = ProductsDetails.objects.get(id=product_id)
                stock = product.product_stock
                product_name = product.product_name
                if int(quantity) <= int(stock):
                    CartTable.objects.filter(user_id=userid, product_id=product_det).update(quantity=quantity)
                    return JsonResponse({'status': "success"})
                elif int(quantity) >= int(stock):
                    return JsonResponse(
                        {'message': "only " + str(stock) + " products available", 'status': "unsuccessful"})
                elif int(stock) == 0:
                    return JsonResponse({'status': "nostock", 'message': "" + str(product_name) + " is Out of stock"})

        else:
            return JsonResponse({'status': "Login to continue"})


"""COUNT THE NO. OF PRODUCTS IN CART"""


def count_cart_products(request):
    if 'userid' not in request.session:
        return redirect('login_redirect')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            products_count = CartTable.objects.filter(user_id=userid).count()
            return products_count
        else:
            return redirect('login_redirect')


"""REMOVE PRODUCT FROM CART"""


def remove_cart_product(request, product_id, cart_id):
    if 'userid' not in request.session:
        return redirect('login_redirect')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            try:
                product = ProductsDetails.objects.get(id=product_id)
                CartTable.objects.get(user_id=userid, product_id=product, id=cart_id).delete()
                return redirect('show_cart')
            except:
                messages.error(request, 'No such product in the cart')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


"""ADD PRODUCTS TO THE WISH LIST TABLE"""


def add_remove_wishlist(request):
    if 'userid' not in request.session:
        return redirect('login_redirect')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            product_id = request.POST.get('product_id')
            product = ProductsDetails.objects.get(id=product_id)
            if product:
                if WishlistTable.objects.filter(user_id=userid, product_id=product).exists():
                    print(".......Already in wishlist........")
                    WishlistTable.objects.get(user_id=userid, product_id=product).delete()
                    print("...........removed from wishlist...")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                else:
                    product_InWishlist = WishlistTable.objects.create(user_id=userid, product_id=product)
                    product_InWishlist.save()
                    print("......Added in wishlist......")
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('login_redirect')


"""TO SHOW WISHLIST ICON FOR PRODUCTS IN WISHLIST TABLE"""


def check_wishlist_icon(request, product_id):
    if 'userid' not in request.session:
        return redirect('login_redirect')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            product = ProductsDetails.objects.get(id=product_id)
            if product:
                if WishlistTable.objects.filter(user_id=userid, product_id=product).exists():
                    wishlist_in = True
                else:
                    wishlist_in = False
                return wishlist_in
        else:
            return redirect('login_redirect')


""" VIEW WISH LIST PAGE"""


def show_wishlist(request):
    if 'userid' not in request.session:
        return redirect('login_redirect')
    else:
        userid = request.session['userid']
        if request.user.is_authenticated:
            wishlist_products = WishlistTable.objects.filter(user_id=userid).order_by('-id')
            return render(request, 'store_WishListPage.html', {'products': wishlist_products})
        else:
            return redirect('login_redirect')


"""LOGIN REDIRECT TO SAME PAGE"""


def login_redirect(request):
    print("..............login to continue.....")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['userid'] = user.id
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            return redirect('store/store_homepage')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login_redirect')
    else:
        return render(request, 'store_LoginPage.html')


"""LOG OUT"""


def logout(request):
    auth.logout(request)
    return redirect('/')
