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
    mobiles = Phone.objects.all()  
    return render(request,"show.html",{'mobiles':mobiles})  
def edit(request, id):  
    mobile = Phone.objects.get(id=id)  
    return render(request,'edit.html', {'employee':mobile})  
def update(request, id):  
    mobile = Phone.objects.get(id=id)  
    form = MobileForm(request.POST, instance = mobile)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': mobile})  
def destroy(request, id):  
    employee = Phone.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  