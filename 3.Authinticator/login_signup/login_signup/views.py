from django.shortcuts import render

def pro_home(request):
    return render(request,'index.html')