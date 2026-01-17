from django.shortcuts import render, redirect

def new_sale(request):
    return render(request, 'sales\create.html')

def sales_history(request):
    return render(request, 'sales\history.html')

def modules(request):
    return render(request, 'sales\modules.html')

def index(request):
    return redirect('modules/')

