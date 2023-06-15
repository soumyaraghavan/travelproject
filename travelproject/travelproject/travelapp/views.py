
from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Pics

# Create your views here.


def demo(request):
    obj=Place.objects.all()
    obj1=Pics.objects.all()
    # name="India"
    # return render(request,"home.html",{'obj':name})
    return render(request,"index.html",{'result':obj,'res':obj1})


# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})
# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return HttpResponse("contact")
