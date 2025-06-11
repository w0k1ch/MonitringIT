from django.urls import path
from . import views


urlpatterns =[
    path('dashboard/', views.index ,name='dashboard-index'),
    path('staff/', views.staff ,name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail,name='dashboard-staff-detail'),
    path('tasks/', views.tasks ,name='dashboard-tasks'),
    path('tasks/delete/<int:pk>/', views.tasks_delete ,name='dashboard-tasks-delete'),
    path('tasks/update/<int:pk>/', views.tasks_update ,name='dashboard-tasks-update'),
    path('execution/', views.execution ,name='dashboard-execution'),
]