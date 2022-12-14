from django.shortcuts import render, redirect  
from mobile.forms import MobileForm  
from mobile.models import Phone  
# Create your views here.  
def phone(request):  
    if request.method == "POST":  
        form = MobileForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = MobileForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    phones = Phone.objects.all()  
    return render(request,"show.html",{'phones':phones})  
def edit(request, id):  
    phone = Phone.objects.get(id=id)  
    return render(request,'edit.html', {'phone':phone})  
def update(request, id):  
    phone = Phone.objects.get(id=id)  
    form = MobileForm(request.POST, instance = phone)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'phone': phone})  
def destroy(request, id):  
    phone = Phone.objects.get(id=id)  
    phone.delete()  
    return redirect("/show")  