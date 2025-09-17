import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('peralatan', 'Peralatan'),
        ('pakaian', 'Pakaian'),
        ('mainan', 'Mainan'),
        ('panjangan', 'Pajangan'),
        ('hiasan', 'Hiasan'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    image = models.URLField(blank=True, null=True)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_trend(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()