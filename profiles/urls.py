from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('detail/', views.profile_detail, name='profile_detail'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('detail/', views.profile_detail, name='detail'),
    path('work_shifts/', views.work_shifts, name='work_shifts'),
]
