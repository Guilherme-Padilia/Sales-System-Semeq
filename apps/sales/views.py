from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse

from .models import Customer, Sale, SaleItem, SalePayment
from ..addresses.models import Address
from ..products.models import Product

import traceback
import requests
import json
from decimal import Decimal

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
    try:
        payload = json.loads(request.body.decode('utf-8'))
        print(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'invalid payload'}, status=400)
        
    customer_data = payload.get('customer')
    address_data  = payload.get('address')
    items         = payload.get('items', [])
    payment       = payload.get('payment')
    
    if not customer_data or not address_data or not items or not payment:
        return JsonResponse({'error': 'invalid payload'}, status=400)
    
    try:
        customer = Customer.objects.get(id=customer_data['id'], is_active=True)
    except Customer.DoesNotExist:
        print(traceback.format_exc())
        return JsonResponse({'error': 'Customer not found'}, status=404)

    try:
        address, created = Address.objects.get_or_create(
            zip_code = address_data.get('cep'),
            street   = address_data.get('street'),
            city     = address_data.get('city'),
            state    = address_data.get('state'),
            number   = address_data.get('number', ''),
        )
        
        print('Inseriu endereço')
    except Address.DoesNotExist:
        print(traceback.format_exc())
        return JsonResponse({'error': 'Address not found'}, status=404)
    
    try:
        sale = Sale.objects.create(
            customer   = customer,
            address    = address,
            subtotal   = Decimal(payload['totals']['subtotal']),
            total_sale = Decimal(payload['totals']['total']),
            status     = 'CONFIRMED'
        )
        
        print('Inseriu Venda')
        
        for item in items:
            try:
                product = Product.objects.get(
                    id=item.get('product_id'),
                    is_active=True
                )
                print('consutlou produto')
            except Product.DoesNotExist:
                print(traceback.format_exc())
                raise Exception(f"Product {item['product_id']} not found")

            quantity   = int(item.get('quantity'))
            unit_price = Decimal(item.get('price'))
            total_price   = quantity * unit_price

            SaleItem.objects.create(
                sale        = sale,
                product     = product,
                quantity    = quantity,
                unit_price  = unit_price,
                total_price = total_price
            )
            
            print('Inseriu item')
    except:
        print(traceback.format_exc())
        return JsonResponse({'error': 'Error creating sale'}, status=500)
    
    try:
        SalePayment.objects.create(
            sale           = sale,
            payment_method = payment.get('type'),
            amount         = payment.get('total'),
            is_active      = True
        )
        
        print('Inseriu pagamento')
    except:
        print(traceback.format_exc())
        
    
    return JsonResponse({'success': True, 'sale_id': sale.id}, status=201)
    
