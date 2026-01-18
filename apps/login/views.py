import traceback
import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import User

def index(request):
    return redirect('login/')

def login_screen(request):
    return render(request, 'login\login.html')

@require_POST
def signin(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
        
        email    = payload.get('email')
        password = payload.get('password')
    except json.JSONDecodeError:
        return JsonResponse({'error': 'invalid payload'}, status=400)

    if not email or not password:
        return JsonResponse({"success": False, "message": "Email and password are required"}, status=400)

    user = User.objects.filter(email=email, password=password).first()

    if user is None:
        return JsonResponse({"success": False, "message": "Invalid credentials"}, status=401)     
        
    return JsonResponse(
        {"success": True, "message": "Login successful"},
        status=200
    )
