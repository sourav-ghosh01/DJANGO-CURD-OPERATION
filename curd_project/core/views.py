from django.shortcuts import render,redirect
from core.models import Student
# Create your views here.
def home(request):
    if request.method=="POST":
       data=request.POST
       f_name=data.get("f_name")
       l_name=data.get("l_name")
       email=data.get("email")
       address=data.get("address")
       phone=data.get("phone")
       Student.objects.create(
           f_name=f_name,
           l_name=l_name,
           email=email,
           address=address,
           phone=phone,
       )
       return redirect(home)
    data=Student.objects.all()
    context={"students":data}
    return render(request,"index.html",context)
def update_student(request,id):
    queryset=Student.objects.get(id=id)
    if request.method=="POST":
       data=request.POST
       f_name=data.get("f_name")
       l_name=data.get("l_name")
       email=data.get("email")
       address=data.get("address")
       phone=data.get("phone")
       queryset.f_name=f_name
       queryset.l_name=l_name
       queryset.email=email
       queryset.address=address
       queryset.phone=phone
       queryset.save()
       return redirect(home)
    context={"students":queryset}
    return render(request,"update.html",context)
def delete_student(request,id):
    queryset=Student.objects.get(id=id)
    queryset.delete()
    return redirect(home)