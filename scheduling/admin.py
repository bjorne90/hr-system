from django.contrib import admin
from .models import WorkShift


class WorkShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_booked', 'role')


admin.site.register(WorkShift, WorkShiftAdmin)