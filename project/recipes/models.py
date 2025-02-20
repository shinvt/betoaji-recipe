from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown
from taggit.managers import TaggableManager

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=30, unique = True)
    description = models.TextField(max_length=4000)
    #image = models.ImageField(upload_to='cusine/', blank=True)
    image = models.FileField(upload_to='cusine/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='recipes_creator', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True,related_name='+', on_delete=models.CASCADE)
    ingredients = models.TextField(max_length=4000,db_column='material')
    instructions = models.TextField(max_length=4000,db_column='methods')
    tags = TaggableManager()
    likedUser = models.ManyToManyField(User, blank=True)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))

    def get_ingredients_as_markdown(self):
        return mark_safe(markdown(self.ingredients, safe_mode='escape'))

    def get_instructions_as_markdown(self):
        return mark_safe(markdown(self.instructions, safe_mode='escape'))
