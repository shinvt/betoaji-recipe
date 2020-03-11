from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Recipe
from ..views import RecipeListView


class HomeTests(TestCase):
    # def setUp(self):
    #     self.board = Board.objects.create(name='Django', description='Django board.')
    #     url = reverse('home')
    #     self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, RecipeListView)
