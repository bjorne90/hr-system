from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import WorkShift
from profiles.models import Profile
from .forms import EventForm
from booking.models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def workshift_list(request):
    user_profile = request.user.profile
    booked_workshifts = user_profile.booked_workshifts.all()
    workshifts = WorkShift.objects.exclude(id__in=booked_workshifts.values_list('id', flat=True))
    return render(request, 'scheduling/workshift_list.html', {'workshifts': workshifts})


@login_required
def book_workshift(request, workshift_id):
    workshift = get_object_or_404(WorkShift, id=workshift_id)

    if request.method == 'POST':
        # Handle the booking logic
        # ...

        if workshift.is_booked:
            # Pass is already booked, display an error message or redirect to a different page
            messages.error(request, 'This pass has already been booked.')
            return redirect('scheduling:workshift_list')

        # Create a new booking object
        booking = Booking.objects.create(user=request.user, workshift=workshift)

        # Update the user's profile with the booked workshift
        user_profile = request.user.profile
        user_profile.booked_workshifts.add(workshift)
        user_profile.save()

        # Update the availability of the pass
        workshift.is_booked = True
        workshift.save()

        # Render a success message
        success_message = 'Du är bokad på detta pass.'
        return render(request, 'scheduling/book_workshift.html', {'workshift': workshift, 'success_message': success_message})

    return render(request, 'scheduling/book_workshift.html', {'workshift': workshift})


@login_required
def work_shifts(request):
    user_profile = request.user.profile
    booked_workshifts = user_profile.booked_workshifts.all()
    return render(request, 'scheduling/work_shifts.html', {'booked_workshifts': booked_workshifts})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scheduling:work_shifts')
    else:
        form = EventForm()
    return render(request, 'scheduling/add_event.html', {'form': form})

def calendar_view(request):
    # Add your calendar view logic here
    return render(request, 'scheduling/calendar.html')
