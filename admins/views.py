from django.shortcuts import render
from .models import Products
from users.models import Purchase
from users.models import Register
from PIL import Image
from django.core.files import File


def alogin(request):
    if request.method=='POST':
        try:
            aemail=request.POST.get('email')
            apassword=request.POST.get('password')
            if aemail=='sakamanikanta3131@gmail.com' and apassword=='3131':
                return render(request,'a_home.html')
            else:
                return render(request,'a_login.html')
        except Exception as err:
            print("EXCEPTION IS:",err)
            return render(request,'a_login.html')
    else:
        return render(request,'a_login.html')


def addproduct(request):
    if request.method=='POST':
        try:
            pname=request.POST.get('pname')
            pcat= request.POST.get('pcat')
            pcost= request.POST.get('pcost')
            pquality= request.POST.get('pquality')
            pdec= request.POST.get('pdec')
            pimage=request.FILES['pimage']

            data=Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage
            )
            data.save()
            return render(request,'view products.html')
        except Exception as err:
            print("EXCEPTION is:",err)
            return render(request,'a_home.html')
    else:
        return render(request, 'add products.html')

def viewproduct(request):
    data = Products.objects.all()
    print(data)
    return render(request, 'view products.html', {'data': data})

def ahome(request):
    return render(request,'a_home.html')


def profile1(request):
    try:
        data=Products.objects.all()
        return render(request,'view products.html',{'profile4':[data]})
    except Exception as err:
        print("EXCEPTION IS:",err)
        return render(request,'add products.html')


def alogout(request):
    return render(request,'a_home.html')



def alastview(request):
    uid=request.session['userid']
    cdata=Register.objects.all()
    cid=cdata
    data=Purchase.objects.all()
    return render(request,'a_lastview.html',{'view':data,'cdata':cdata})