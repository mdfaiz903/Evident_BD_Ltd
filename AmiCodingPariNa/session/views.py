from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
# Create your views here.
def signup(request):
    if request.method=='POST':
        user_name = request.POST['Username']
        f_name = request.POST['F_name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        data = User.objects.create_user(username= user_name,first_name=f_name,last_name=l_name,email=email,password=password1)

        data.save()
        return redirect('session/login.html')
    return render(request,'session/signup.html')

def Login(request):
    if request.method=='POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        
    return render(request,'session/login.html')

