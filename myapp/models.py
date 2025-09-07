from django.db import models
from django.contrib.auth.models import User


# -----------------------------
# Product Model
# -----------------------------
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Flexible for cents/paise
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


# -----------------------------
# Feedback Model
# -----------------------------
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    feedback_msg = models.TextField()
    updated_datetime = models.DateTimeField(auto_now=True)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} --- {self.feedback_msg[:30]}"  # show only 30 chars


# -----------------------------
# Cart Model
# -----------------------------
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"


# -----------------------------
# Billing Model
# -----------------------------
class Billing(models.Model):
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Billing - {self.username} ({self.total_amount})"
