from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required

def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
        booked_workshifts = profile.booked_workshifts.all()
    except Profile.DoesNotExist:
        profile = None
        booked_workshifts = None
    return render(request, 'profiles/profile_detail.html', {'profile': profile, 'booked_workshifts': booked_workshifts})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Process form submission
        # Update the profile with the form data
        profile.phone_number = request.POST['phone_number']
        profile.address = request.POST['address']

        # Handle profile image upload
        if request.FILES.get('profile_image'):
            profile.profile_image = request.FILES['profile_image']

        profile.save()
        return redirect('profiles:profile_detail')
    else:
        return render(request, 'profiles/edit_profile.html', {'profile': profile})

def user_login(request):
    # Login logic
    # ...

    return redirect(reverse('profiles:profile_detail'))

@login_required
def profile(request):
    user_profile = request.user.profile
    booked_workshifts = user_profile.booked_workshifts.all()
    return render(request, 'profiles/profile.html', {'booked_workshifts': booked_workshifts})

@login_required
def work_shifts(request):
    user_profile = request.user.profile
    booked_workshifts = Booking.objects.filter(user=user_profile.user)
    return render(request, 'profiles/profile_detail.html', {'booked_workshifts': booked_workshifts})

def staff_list(request):
    employees = Profile.objects.all()
    return render(request, 'profiles/staff_list.html', {'employees': employees})
