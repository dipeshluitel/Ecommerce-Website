from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'goCart/home.html')

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category = val)
        return render(request, 'goCart/category.html',locals())