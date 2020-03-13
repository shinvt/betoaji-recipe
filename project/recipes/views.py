from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.views.generic import UpdateView, ListView
from .models import Recipe
from django.utils import timezone
from .forms import NewRecipeForm
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    if request.user.is_authenticated:
        recipes = get_list_or_404(Recipe)
        return render(request, 'recipes.html', {'recipes' : recipes})
    else:
        return render(request, 'home.html')

# Create your views here.
@method_decorator(login_required, name='dispatch')
class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes.html'


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
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

@method_decorator(login_required, name='dispatch')
class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['description','image','ingredients','instructions']
    template_name = 'edit_recipe.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'recipe'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.updated_by = self.request.user
        recipe.updated_at = timezone.now()
        recipe.save()
        return redirect('recipe_detail', pk=recipe.pk)
