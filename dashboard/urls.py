from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
   path('dashboard/', views.dashboard, name='dashboard'),
   path('', RedirectView.as_view(url='project_dashboard/', permanent=False)),
   # path('projects/', views.select_monthly_plan, name='project_dashboard'),
   path('project_dashboard/', views.project_dashboard, name='project_dashboard'),
   path('monthly/', views.select_monthly_plan, name='monthly'),
   path('yearly/', views.select_yearly_plan, name='yearly'),
   path("script/", views.run_script, name="scripts"),
   path('test/', views.test, name='test'),
]