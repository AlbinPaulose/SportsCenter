from django.contrib import admin
from .models import categories, ProductsDetails
from django.contrib.auth.models import User, auth
from django import forms


# Register your models here.

@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    list_display = ("category", "subcategory", "childcategory")


@admin.register(ProductsDetails)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name", "category", "subcategory", "childcategory", "product_size", "product_color",
        "product_gender_for",
        "product_stock")

#
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = ProductDetails
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['childcategory'].queryset = categories.objects.values_list('childcatefory',flat=True)
#
#     # def get_form(self, request, obj=None, **kwargs):
#     #     form = super().get_form(request, obj, **kwargs)
#     #     sub_category = form.base_fields["subcategory"].label
#     #     print("................", sub_category)
#     #     result = categories.objects.filter(subcategory=sub_category)
#     #     return form
