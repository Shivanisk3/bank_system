from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request, 'users/home.html')

def transfer(request):
    customer = Customer.objects.all()
    j='null'
    if request.method=="POST":
        email=request.POST['email']
        amt=request.POST['amount']
        rec=request.POST['rec']
        print(email)
        print(amt)
        print(rec)
        amt=int(amt)
        
        if email == 'select' or rec == 'select' or (email=='select' and rec=='select') or rec==email:
            messages.warning(request,"Email Id not selected or both Email Ids are same")  
        elif amt <= 0:
            messages.warning(request,'Please provide valid transfer amount!!')
        else:
            for c in customer:
                if c.email==email:
                    j=email
                    i=c.id
                    name=c.name
                    if amt > c.bal:
                        messages.warning(request,"Insufficient Balance!!")   
                    break

        for x in customer:
            if x.email==rec:
                rid=x.id
                rname=x.name
                rbal=x.bal
                break
 
        for c in customer: 
            if c.email==email and rec!=email and rec!='select' and amt<=c.bal and amt>0:
                q1= History(sender=name,reciever=rname,amount=amt)
                bal=c.bal-amt
                q2= Customer.objects.filter(id=i).update(bal=bal)
                q1.save()
                bal=rbal+amt
                q3=Customer.objects.filter(id=rid).update(bal=bal)
                messages.success(request,"Transferred successfully!!")
                return redirect('record')
                
    return render(request,'users/transfer.html',{'customer':customer})

def record(request):
    tr = History.objects.all()
    return render(request, 'users/record.html',{'tr':tr})

def details(request):
    customer = Customer.objects.all()
    return render(request,'users/customers.html',{'customer':customer})