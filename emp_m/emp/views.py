from django.shortcuts import render, redirect
from .models import Employee_Info

# Create your views here.

def base(request):
    return render(request, "base.html")

def home(request):
    emp = Employee_Info.objects.all()
    return render(request, "home.html", {'emp': emp})

def add_emp(request):
    emp = Employee_Info()
    if request.method=="POST":
        full_name = request.POST.get("full_name")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        image = request.FILES.get("image")
        position = request.POST.get("position")
        address = request.POST.get("address")

        emp = Employee_Info()

        emp.full_name = full_name
        emp.gender = gender
        emp.email = email
        emp.phone = phone
        emp.image = image
        emp.position = position
        emp.address = address

        emp.save()
        return redirect("home")

    return render(request, "add_emp.html")

def update_emp(request):
    return render(request, "update_emp.html")