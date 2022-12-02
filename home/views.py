from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from cars.models import Car


def home_view(request):
    return render(request, 'home/landing-page.html')


class SearchResultsView(ListView):
    model = Car
    template_name = 'home/search-results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('categories')
        object_list = Car.objects.all().filter(location=query, category=category)
        return object_list

