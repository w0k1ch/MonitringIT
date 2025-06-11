from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tasks,Execution
from .forms import TasksForm, ExecutionForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


@login_required
def index(request):
    executions = Execution.objects.all()
    tasks = Tasks.objects.all()
    executions_count = executions.count()
    tasks_count = tasks.count()
    workers_count = User.objects.all().count()
    if request.method=='POST':
        form = ExecutionForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = ExecutionForm()
    context={
        'executions': executions,
        'form': form,
        'tasks': tasks,
        'tasks_count':tasks_count,
        'workers_count': workers_count,
        'executions_count': executions_count,

    }
    return render(request,'dashboard/index.html',context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    executions_count = Execution.objects.all().count()
    tasks_count = Tasks.objects.all().count()
    context={
        'workers':workers,
        'workers_count': workers_count,
        'executions_count': executions_count,
        'tasks_count': tasks_count,
    }
    return render(request,'dashboard/staff.html',context)

def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def tasks(request):
    items = Tasks.objects.all()
    tasks_count = items.count()
    #items = Tasks.objects.raw('SELECT * FROM dashboard_tasks')
    workers_count = User.objects.all().count()
    executions_count = Execution.objects.all().count()

    if request.method =='POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            Tasks_name = form.cleaned_data.get('name')
            messages.success(request, f'{Tasks_name} был добавлен')
            return redirect('dashboard-tasks')
    else:
        form = TasksForm()
    context = {
        'items': items,
        'form':form,
        'workers_count' : workers_count,
        'executions_count': executions_count,
        'tasks_count':tasks_count
    }
    return render(request, 'dashboard/tasks.html', context)

@login_required
def tasks_delete(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-tasks')
    return render(request, 'dashboard/tasks_delete.html')

@login_required
def tasks_update(request, pk):
    item = Tasks.objects.get(id=pk)
    if request.method=='POST':
        form = TasksForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-tasks')
    else:
        form = TasksForm(instance=item)
    context={
        'form': form,
    }
    return render(request, 'dashboard/tasks_update.html', context)

@login_required
def execution(request):
    executions = Execution.objects.all()
    executions_count = executions.count()
    workers_count = User.objects.all().count()
    tasks_count = Tasks.objects.all().count()
    context={
        'executions': executions,
        'workers_count': workers_count,
        'executions_count':executions_count,
        'tasks_count':tasks_count,
    }
    return render(request,'dashboard/execution.html', context)