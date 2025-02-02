from django.shortcuts import render,redirect
from home.models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login
from django.http import JsonResponse,HttpResponse
from .utils import is_ajax, classify_face
import base64
from logs.models import Log
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"home.html")

def profile(request):
    profile=request.user
    context={'user':profile}
    return render(request,'profile.html',context)

def registration(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('birthday')
        state=request.POST.get('state')
        city=request.POST.get('city')
        profession=request.POST.get('Profession')
        skill=request.POST.get('skill')
        password=make_password(request.POST.get('password'))
        photo=request.FILES.get('photo')
        
        if photo:
            print("Photo is not null")
        else:
            print("Photo is null")

        user=CustomUser.objects.filter(username=username)

        if user.exists():
            messages.info(request, "This Username has already been taken.")
            return redirect('/register/')
        
        user=CustomUser.objects.filter(email=email)

        if user.exists():
            messages.info(request, "This Email has already been taken.")
            return redirect('/register/')

        ins=CustomUser(first_name=first_name,
                       last_name=last_name,
                       username=username,
                       phone=phone,
                       email=email,
                       address=address,
                       gender=gender,
                       dob=dob,
                       state=state,
                       city=city,
                       profession=profession,
                       skill=skill,
                       password=password,
                       photo=photo)
        ins.save()
        messages.success(request, "Your account has been created successfully.")
    return render(request,"register.html")

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=CustomUser.objects.filter(username=username)

        if not user.exists():
            messages.error(request,'Invalid username')
            return redirect('/login/')
        
        user = CustomUser.objects.get(username=username)
        password_correct = check_password(password, user.password)
        if password_correct:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/profile/')
        else:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
    return render(request,'login1.html')


def log_view(request):
    return render(request,'login.html') 

def find_user_view(request):
    if is_ajax(request):
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        # print(photo)
        decoded_file = base64.b64decode(str_img)

        x = Log()
        x.photo.save('upload.png', ContentFile(decoded_file))
        x.save()

        res = classify_face(x.photo.path)
        if res:
            user_exists = CustomUser.objects.filter(username=res).exists()
            if user_exists:
                user = CustomUser.objects.get(username=res)
                profile = CustomUser.objects.get(username=user.username)
                x.profile = profile
                x.save()

                login(request,user)
                print("sucessful login")
                messages.success(request, 'Login successful.')
                html_element="<html><body><h1>Login Succesful</h1></body></html>"
                return  HttpResponse(html_element)
            else:
                print("unsucessful attempt")
                messages.success(request, 'Login unsuccessful.')

        html_ele="<html><body><h1>Login not Succesful</h1></body></html>"  
        return  HttpResponse(html_ele)
    
def cv_generate(request):
    return render(request,'resume.html')
