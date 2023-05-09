from django.shortcuts import render
from .models import WorkShift
from .forms import EventForm

def workshift_list(request):
    workshifts = WorkShift.objects.all()
    return render(request, 'scheduling/workshift_list.html', {'workshifts': workshifts})

def book_workshift(request, workshift_id):
    workshift = WorkShift.objects.get(id=workshift_id)
    
    if request.method == 'POST':
        # Save the booking logic here
        # For example, you can add the shift to the user's profile
        
        # Assuming you have a UserProfile model with a shifts field
        user_profile = request.user.profile
        user_profile.shifts.add(workshift)
        
        messages.success(request, 'Du är bokad på detta pass.')
        return redirect('scheduling:workshift_list')
    
    context = {'workshift': workshift}
    return render(request, 'scheduling/book_workshift.html', context)

def work_shifts(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # Process the form data and save the event
            # Example: event = Event(title=form.cleaned_data['title'], start_date=form.cleaned_data['start_date'], end_date=form.cleaned_data['end_date'])
            # event.save()
            return redirect('scheduling:work_shifts')

    context = {'form': form}
    return render(request, 'scheduling/work_shifts.html', context)

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