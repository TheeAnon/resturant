from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    name_pl = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_pl = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    description_pl = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name