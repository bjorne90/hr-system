from django.urls import path
from . import views

app_name = 'scheduling'

urlpatterns = [
    path('list/', views.workshift_list, name='workshift_list'),
    path('book/<int:workshift_id>/', views.book_workshift, name='book_workshift'),
    path('work-shifts/', views.work_shifts, name='work_shifts'),
    path('work-shifts/add-event/', views.add_event, name='add_event'),
    path('calendar/', views.calendar_view, name='calendar'),
]
