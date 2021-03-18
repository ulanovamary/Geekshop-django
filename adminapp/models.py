from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(('active'),default=True)

    def __str__(self):
        return self.name