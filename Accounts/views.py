from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'Accounts/login.html')

def register_page(request):
    return render(request, 'Accounts/register.html')    

