from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('detail/', views.profile_detail, name='profile_detail'),
    path('edit/', views.edit_profile, name='edit_profile'),
    # Add the following line
    path('detail/', views.profile_detail, name='detail'),
]
