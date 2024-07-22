from django.shortcuts import render, redirect
from .models import Bag
from .forms import SearchForm
from .serializers import BagSerializers
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

@api_view(['GET'])
def BagView(request):
    list_bag = Bag.objects.all()
    bag_serializer = BagSerializers(list_bag , many=True)
    context = {"list_data": bag_serializer}
    return render(request, "./product.html", context)


def SearchView(request):
    form = SearchForm()
    results = []
    if request.method == "POST" or "GET":
        
        if "query" in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data["query"]
                results = Bag.objects.filter(bag_name__icontains=query)
    return render(request, "search.html", {"form": form, "results": results})
