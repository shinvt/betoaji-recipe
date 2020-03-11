from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from .models import Recipe
from django.utils import timezone
from .forms import NewRecipeForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'home.html'


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def new_recipe(request):
    if request.method == 'POST':
        form = NewRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_at = timezone.now()
            recipe.created_by = request.user
            recipe.updated_at = timezone.now()
            recipe.updated_by = request.user
            recipe.save()
            return redirect('recipe_detail',pk=recipe.pk)
    else:
        form = NewRecipeForm()
    return render(request, 'new_recipe.html', {'form': form})
