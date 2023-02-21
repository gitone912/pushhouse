from django.urls import path
from . import views

urlpatterns = [
   # path('overview', views.overview, name='overview'),
   path('overview', views.user_data, name='overview'),
   path('edit_profile/', views.edit_user_data, name='edit_user_data'),
]