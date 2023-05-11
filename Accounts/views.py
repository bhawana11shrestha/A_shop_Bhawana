from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def login_page(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

#if user already exists.......
        user_obj = User.objects.filter(username = email)
        
        if not user_obj.exists():  #If user does not exist........
            messages.warning(request,"Account not found")
            return HttpResponseRedirect(request.path_info) #Redirecting on same page.........

            if user_obj[0].profile.is_email_verified:
                messages.warning(requet,'your account is nt verified')
                return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email, password = password)
        if user_obj:  #If user exists...............
            login(request, user_obj)
            return redirect('/')

        messages.warning(request,"Invalid Credential")      
        return HttpResponseRedirect(request.path_info)

    return render(request, 'Accounts/login.html')

def register_page(request):
    if request.method== 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

#if user already exists.......
        user_obj = User.objects.filter(username = email)
        
        if user_obj.exists():
            messages.warning(request, "Email is already taken.")
            return HttpResponseRedirect(request.path_info) #Redirecting on same page.........
            
            #else Creating new user and setting password............
        user_obj = User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)  
        user_obj.set_password(password)
        user_obj.save()


        messages.success(request,"Email has been sent, please check it out")      
        return HttpResponseRedirect(request.path_info)


    return render(request, 'Accounts/register.html')    

