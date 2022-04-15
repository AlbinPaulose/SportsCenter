from django.db import models

# Create your models here.
subcategories = (
    ("team sports", "Team Sports"),
    ("footwear", "Footwear"),
    ("cycling", "Cycling"),
    ("gym accessories", "Gym Accessories"),
    ("activewear", "Activewear"),
    ("sports sunglasses", "Sports Sunglasses")
)
childcategories = (
    ("football", "Football"),
    ("cricket", "Cricket"),
    ("basketball", "Basketball"),
    ("volleyball", "Volleyball"),
    ("hockey", "Hockey"),
)

product_used_for = (
    ("men", "Men"), ("women", "Women"), ("all", "All")
)


class categories(models.Model):
    category = models.CharField(default='all sports', max_length=20)
    subcategory = models.CharField(max_length=20, choices=subcategories)
    childcategory = models.CharField(max_length=20)

    def __str__(self):
        return self.childcategory


class ProductsDetails(models.Model):
    category = models.CharField(default='all sports', max_length=20)
    subcategory = models.CharField(max_length=30, choices=subcategories)
    childcategory = models.ForeignKey(categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_gender_for = models.CharField(max_length=10, choices=product_used_for)
    product_offer = models.BooleanField(default=False)
    product_offer_details = models.CharField(max_length=50, default='no offer')
    product_actual_price = models.IntegerField(blank=True)
    product_selling_price = models.IntegerField()
    product_size = models.CharField(max_length=20)
    product_stock = models.IntegerField()
    product_brand = models.CharField(max_length=35)
    product_color = models.CharField(max_length=25, blank=True)
    product_image = models.ImageField(upload_to='product_images')
    product_addondate = models.DateField(auto_now_add=True)
    product_details = models.TextField(blank=True,max_length=200)