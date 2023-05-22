from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import WorkShift, Booking
from scheduling.views import send_email_notification

class BookingInline(admin.TabularInline):
    model = Booking
    extra = 1

class WorkShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_booked', 'role')
    list_display_links = ('name',)
    inlines = [BookingInline]

    def assign_user(self, request, queryset):
        for workshift in queryset:
            if not workshift.is_booked:
                # Retrieve all users
                users = User.objects.all()

                # Create a new booking object for each user
                for user in users:
                    booking = Booking.objects.create(user=user, workshift=workshift)
                    send_email_notification(workshift, user)

                # Update the availability of the workshift
                workshift.is_booked = True
                workshift.save()

    assign_user.short_description = "Assign users to selected workshifts"

admin.site.register(WorkShift, WorkShiftAdmin)
