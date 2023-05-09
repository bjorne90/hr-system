from django.shortcuts import render, redirect
from .models import Pass

def booking_list(request):
    passes = Pass.objects.filter(user=request.user)
    return render(request, 'booking/booking_list.html', {'passes': passes})

def book_pass(request):
    if request.method == 'POST':
        # Process form submission
        # Create a new pass based on the form data
        new_pass = Pass(user=request.user, place=request.POST['place'], time=request.POST['time'], role=request.POST['role'])
        new_pass.save()
        return redirect('booking:booking_list')
    else:
        return render(request, 'booking/book_pass.html')
