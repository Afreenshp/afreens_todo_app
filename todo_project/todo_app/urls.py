
from django.urls import path, include
from . import views

urlpatterns = [

    # path('task',views.get_task,name='get_task'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('',views.display_task,name='display_task'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvtask/', views.TaskListView.as_view(), name='cbvtask'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]
