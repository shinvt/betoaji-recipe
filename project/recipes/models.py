from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=30, unique = True)
    description = models.TextField(max_length=4000)
    #image = models.ImageField(upload_to='cusine/', blank=True)
    image = models.FileField(upload_to='cusine/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True,related_name='+', on_delete=models.CASCADE)
    ingredients = models.TextField(max_length=4000,db_column='material')
    instructions = models.TextField(max_length=4000,db_column='methods')

    def __str__(self):
        return self.name

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))

    def get_material_as_markdown(self):
        return mark_safe(markdown(self.material, safe_mode='escape'))

    def get_methods_as_markdown(self):
        return mark_safe(markdown(self.methods, safe_mode='escape'))
