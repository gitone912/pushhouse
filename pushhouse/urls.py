from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboard urls
    path('', include('dashboard.urls')),

    # Auth urls
    path('', include('account.urls')),
    path('', include('authentication.urls')),
]

handler404 = TemplateView.as_view(template_name='pages/system/not-found.html')
handler500 = TemplateView.as_view(template_name='pages/system/error.html')
