from atexit import register
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .models import Algorithm


def index_view(request,*args,**kwargs):
    return render(request,"index.html", {})

def lab_view(request,*args,**kwargs):
    return render(request,"#", {})

def assesment_view(request,*args,**kwargs):
    return render(request,"#", {})

def experiment_view(request,*args,**kwargs):
    
    return render(request,"#", {})

# TRAIL TRAIL


def algorithm_list(request):
    algorithms = Algorithm.objects.filter(user=request.user)
    return render(request, '', {'algorithms': algorithms})


def algorithm_create(request):
    if request.method == 'POST':
        algorithm = Algorithm(user=request.user,
                              name=request.POST['name'],
                              code=request.POST['code'])
        algorithm.save()
        return redirect('algorithm_list')
    return render(request, '')


def algorithm_delete(request, pk):
    algorithm = Algorithm.objects.get(pk=pk)
    if request.user != algorithm.user:
        return redirect('algorithm_list')
    algorithm.delete()
    return redirect('algorithm_list')


# ALGORITHMS

