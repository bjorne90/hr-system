from django.db import models

class WorkShift(models.Model):
    # Define the fields of the WorkShift model
    # For example:
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def workshift_list(request):
    from booking.models import Booking
    workshifts = Booking.objects.values('workshift').distinct()
    return render(request, 'scheduling/workshift_list.html', {'workshifts': workshifts})

@login_required
def book_workshift(request, workshift_id):
    from booking.models import Booking
    workshift = Booking.objects.get(id=workshift_id).workshift

    if request.method == 'POST':
        # Handle the booking logic
        # ...

        # Update the user's profile with the booked workshift
        user_profile = request.user.profile_profile
        user_profile.booked_workshifts.add(workshift)
        user_profile.save()

        # Render a success message
        success_message = 'Du är bokad på detta pass.'
        return render(request, 'scheduling/book_workshift.html', {'workshift': workshift, 'success_message': success_message})

    return render(request, 'scheduling/book_workshift.html', {'workshift': workshift})

@login_required
def work_shifts(request):
    from booking.models import Booking
    user_profile = request.user.profile_profile
    booked_workshifts = Booking.objects.filter(user_profile=user_profile)
    return render(request, 'scheduling/work_shifts.html', {'booked_workshifts': booked_workshifts})

@login_required
def add_event(request):
    # Handle adding event logic
    return render(request, 'scheduling/add_event.html')
