from django import forms
from .models import Recipe

class NewRecipeForm(forms.ModelForm):
     class Meta:
        model = Recipe
        fields = ['name',
                  'description',
                  'image',
                  'ingredients',
                  'instructions',
                  ]
