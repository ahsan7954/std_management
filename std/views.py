from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    std = Student.objects.all()
    return render(request,'std/home.html', {'std':std})

def std_add(request):
    if request.method == "POST":
        std_roll = request.POST.get('std_roll')
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_address = request.POST.get('std_address')
        std_phone = request.POST.get('std_phone')
        s = Student(roll=std_roll, name=std_name, email=std_email, address=std_address, phone=std_phone)
        s.save()
        return redirect('/std/home/')
         
    return render(request, 'std/add-std.html', {})

def std_delete(request, roll):
    s = Student.objects.get(pk=roll)
    s.delete()

    return redirect("/std/home")

def std_update(request, roll):
    std = Student.objects.get(pk=roll)
    return render(request, "std/update-std.html", {'std':std})

def do_std_update(request, roll):
    std_roll = request.POST.get('std_roll')
    std_name = request.POST.get('std_name')
    std_email = request.POST.get('std_email')
    std_address = request.POST.get('std_address')
    std_phone = request.POST.get('std_phone')

    std = Student.objects.get(pk=roll)
    std.roll = std_roll
    std.name = std_name
    std.email = std_email
    std.address = std_address
    std.phone = std_phone
    std.save()

    return redirect("/std/home")