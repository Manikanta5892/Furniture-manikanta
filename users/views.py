from django.shortcuts import render,redirect
from .models import Register
from admins.models import Products
from .models import Purchase
from django.contrib import messages

# Create your views here.
def reg(request):
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        p=request.POST.get('password')
        m=request.POST.get('mobile')
        a=request.POST.get('address')
        pc1=request.POST.get('pincode')
        data=Register(
            name=n,
            email=e,
            password=p,
            mobile=m,
            address=a,
            pincode=pc1
        )
        data.save()
        return render(request,'index.html')
    else:
        return render(request,'register.html')


def log(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            password=request.POST.get('password')
            data=Register.objects.get(email=email,password=password)
            request.session['userid']=data.email
            print(data)
            return render(request,'u_home.html')
        except Exception as err:
            print("exception is:",err)
            return render(request,'login.html')
    else:
        return render(request,'login.html')



def home(request):
    return render(request,'u_home.html')


def profile(request):
    try:
        uid=request.session['userid']
        print(uid)
        data=Register.objects.get(email=uid)
        return render(request,'u_profile.html',{'profile':[data]})
    except Exception as E:
        print("exception is:",E)
        return render(request,'u_profile.html')


def index(request):
    return render(request,'index.html')

def products(request):
    data = Products.objects.all()
    return render(request,'u_product.html',{'products': data})

def buyproduct(request,id):
    if request.method == 'POST':
        uid = request.session['userid']
        cid = Register.objects.get(email=uid)

        product = Products.objects.get(id=id)
        data = Purchase(
            pname=product.pname,
            pcost=product.pcat,
            pcat=product.pcat,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=cid.id,
            pid_id=id
        )
        data.save()
        messages.success(request,'SUCESSFULLY PURCHASED')
        return render(request, 'u_product.html')
    else:
        messages.error(request,'NOT PURCHASED')
        return redirect('products', id=id)

def purchase(request):
    uid = request.session['userid']
    cdata = Register.objects.get(email=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    return render(request, 'u_purchase.html', {'data': data,'cdata':cdata})


def lastview(request):
    uid = request.session['userid']
    cdata = Register.objects.get(email=uid)
    cid = cdata.id
    data=Purchase.objects.filter(cid_id=cid)
    return render(request,'last_view.html',{'view':data,'cdata':cdata})

def logout(request):
    return render(request,'index.html')


def HOME(request):
    return render(request,'HOME.html')


def categories(request):
    return render(request,'categories.html')


def pmsg(request):
    return render(request,'pmsg.html')