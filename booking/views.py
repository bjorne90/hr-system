from django.shortcuts import render, redirect, get_object_or_404
from .models import Pass
from datetime import datetime
from scheduling.models import WorkShift
from django import forms
from .models import Booking

def booking_list(request):
    passes = Pass.objects.filter(user=request.user).select_related('workshift')
    return render(request, 'booking/booking_list.html', {'passes': passes})


class PassForm(forms.Form):
    place = forms.CharField()
    time = forms.CharField()
    role = forms.CharField()

def book_pass(request, workshift_id):
    workshift = get_object_or_404(WorkShift, id=workshift_id)
    
    if not workshift.is_booked:
        new_pass, created = Pass.objects.get_or_create(user=request.user, workshift=workshift)
        
        if created:
            return redirect('booking:booking_list')
        else:
            # Pass already exists, display an error message or redirect to a different page
            return redirect('scheduling:workshift_list')
    else:
        # Pass is already booked, display an error message or redirect to a different page
        return redirect('scheduling:workshift_list')
