from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def register(request):
    return render(request, 'accounts/register.html')
# @login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')