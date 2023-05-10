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

@login_required
def cancel_workshift(request, workshift_id):
    workshift = get_object_or_404(WorkShift, id=workshift_id)

    if request.method == 'POST':
        # Check if the workshift is already booked
        if not workshift.is_booked:
            messages.error(request, 'This workshift is not booked.')
            return redirect('scheduling:work_shifts')

        # Get the current user's profile
        user_profile = request.user.profile

        # Check if the user has booked the workshift
        if workshift not in user_profile.booked_workshifts.all():
            messages.error(request, 'You have not booked this workshift.')
            return redirect('scheduling:work_shifts')

        # Remove the workshift from the user's booked workshifts
        user_profile.booked_workshifts.remove(workshift)
        user_profile.save()

        # Update the availability of the workshift
        workshift.is_booked = False
        workshift.save()

        messages.success(request, 'Workshift canceled successfully.')
        return redirect('scheduling:work_shifts')

    # Handle GET request (show confirmation page)
    return render(request, 'scheduling/cancel_workshift.html', {'workshift': workshift})

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
    shifts = WorkShift.objects.filter(is_booked=False)
    return render(request, 'scheduling/calendar2.html', {'shifts': shifts})

