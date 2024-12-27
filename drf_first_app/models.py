from django.db import models

# Create your models here.
class Category(models.Model):
    category_code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True, max_length=200) 

    def __str__(self):
        return self.name
    