from django.contrib import admin
from .models import WorkShift

class WorkShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_booked', 'role')
    list_display_links = ('name',)  # Add the field you want to link to the change view

    def remove_user(self, obj):
        if obj.is_booked:
            obj.user = None
            obj.is_booked = False
            obj.save()

    remove_user.short_description = "Remove User from Shift"

    actions = ['remove_user']

admin.site.register(WorkShift, WorkShiftAdmin)
