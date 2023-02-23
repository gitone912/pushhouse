from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='dashboard'),
   # path('projects/', views.select_monthly_plan, name='project_dashboard'),
   path('project_dashboard/', views.project_dashboard, name='project_dashboard'),
   path('monthly/', views.select_monthly_plan, name='monthly'),
   path('yearly/', views.select_yearly_plan, name='yearly'),
]