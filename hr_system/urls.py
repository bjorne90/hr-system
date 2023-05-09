from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('booking/', include('booking.urls')),
    path('profiles/', include('profiles.urls')),
    path('scheduling/', include('scheduling.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]

