from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def search_products(request):
    data = []
    name_search = request.GET.get('pname')
    
    if name_search:
        products = Product.objects.filter(
            name__icontains=name_search,
            is_active=True
        )
    else:
        products = Product.objects.filter(
            is_active=True    
        )
    
    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "supplier": product.supplier.name
        })
        
    return JsonResponse(data, safe=False)
