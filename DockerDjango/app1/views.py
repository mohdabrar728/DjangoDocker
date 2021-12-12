from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<center><h1>Welcome Dockerize Django Project</h1></center>')