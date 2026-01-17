from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from .models import Customer

import requests

def new_sale(request):
    return render(request, 'sales\create.html')

def sales_history(request):
    return render(request, 'sales\history.html')

def modules(request):
    return render(request, 'sales\modules.html')

def index(request):
    return redirect('modules/')


@require_GET
def search_customer(request):
    data = []
    name_search = request.GET.get('name')
    
    if name_search:
        customers = Customer.objects.filter(
            name__icontains=name_search,
            is_active=True
        )
    else:
        customers = Customer.objects.filter(
            is_active=True    
        )
    
    for customer in customers:
        data.append({
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone
        })
        
    return JsonResponse(data, safe=False)

@require_GET
def search_address_by_cep(request):
    data = []
    cep = request.GET.get('cep')   
    
    if not cep:
        return JsonResponse(data, safe=False)
    
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    
    if response.status_code == 200:
        address = response.json()
    
    return JsonResponse(address, safe=False)

@require_POST
def create_sale(request):
    data = request.body.decode('utf-8')
    
    if not data:
        data = {
            "error": "Dados inválidos"
        }
        return JsonResponse(data, safe=False).status_code == 400
    
    return JsonResponse(data, safe=False)
    
