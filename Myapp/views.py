from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import cars

# Create your views here.

def home(request):
    c1 = cars.objects.all()
    return render(request, 'Home.html',{'show':c1})

def add(request):
    try:
        dis = ''
        if request.method=='POST':
            c1 = request.POST['city']
            c2 = request.POST['carname']
            c3 = request.POST['carprice']
            c4 = request.POST['company']
            add = cars(City=c1,CarName=c2,CarPrice=c3,Company=c4).save()
            # dis = c1,c2,c3,c4
            # print(dis)
            return redirect('/')
    except:
        pass
    return render(request, 'Add.html')

def delete(request, id):
    car = get_object_or_404(cars, id=id)
    car.delete()
    return redirect('/')
