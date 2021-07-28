from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from ecommerceapp.models import Product, Category


def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products=Product.objects.filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
        cats=Category.objects.all()
    return render(request,'category.html',{'category':c_page,'products':products})

def ProdCatDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Details!')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        if username or password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                messages.info(request,"User Created")
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request,'Invalid Details')
            return redirect('register')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')