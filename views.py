from django.shortcuts import render,redirect
from .models import project,city
from .forms import ProjectForm
from django.db.models import Q
# Create your views here.
def say_hello(request):
    return render (request,'hello.html',{'name':'Rogers'})

#rooms=[
 #   {'id':1,'name':'Lets fuck it'},
 #   {'id':2,'name':'Design with me'},
 #   {'id':3,'name':'fuck it'},
 #   ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    projects = project.objects.filter(
        Q(city__name__icontains=q)|Q(name__icontains=q))
    project_count = projects.count()
    citys = city.objects.all()
    context = {'projects':projects,'citys':citys ,'project_count':project_count}
    return render(request,'team6/home.html',context)

def projects(request, pk):
    projects = project.objects.get(id = pk)
    context = {'project':projects}
    return render(request,'team6/project.html',context)

def createproject(request):
    form= ProjectForm()
    if request.method == 'POST':
       form = ProjectForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    context = {'form':form}
    return render(request , 'team6/project_form.html',context)

def updateproject(request,pk):
    projects = project.objects.get(id = pk)
    form = ProjectForm(instance = project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,instance = projects)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render (request,'team6/project_form.html',context)

def deleteproject(request,pk):
    projects = project.objects.get(id = pk)
    if request.method == 'POST':
        projects.delete()
        return redirect('home')
    return render (request,'team6/delete.html',{'obj':projects})