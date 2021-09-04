from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import task
from .forms import ToDoforms

# Create your views here.
# def get_task(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = task(name=name, priority=priority)
#         obj.save()
#     return render(request, 'task.html')

class TaskListView(ListView):
    model = task
    template_name = 'Display_Task.html'
    context_object_name = 'obj'

class TaskDetailView(DetailView):
    model = task
    template_name = 'Details.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields= ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')

def display_task(request):
    obj1=task.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = task(name=name, priority=priority,date=date)
        obj.save()

    return render(request, 'Display_Task.html',{'obj':obj1})

def delete(request,task_id):
    task1=task.objects.get(id=task_id)
    if request.method=="POST":
        task1.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task1})

def update(request,id):
    task1=task.objects.get(id=id)
    form= ToDoforms(request.POST or None, instance=task1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'task': task1,'form':form})