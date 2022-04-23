from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'basic_app/landing.html')

def log_in(request):
    return render(request,'basic_app/log_in.html')

def reg(request):
    return render(request,'basic_app/reg.html')
