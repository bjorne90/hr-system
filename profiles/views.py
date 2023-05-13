from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Profile
from booking.models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
        booked_workshifts = profile.booked_workshifts.all()
        return render(request, 'profiles/profile_detail.html', {'profile': profile, 'booked_workshifts': booked_workshifts})
    except Profile.DoesNotExist:
        return render(request, 'profiles/create_profile.html')


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Update the profile with the form data
        profile.phone_number = request.POST.get('phone_number')
        profile.email = request.POST.get('email')
        profile.user.set_password(request.POST.get('password'))
        profile.user.save()
        profile.about_me = request.POST.get('about_me')
        profile.profile_image = request.FILES.get('profile_image')

        # Save the updated profile
        profile.save()

        # Construct the URL for the profile_detail view using the reverse function
        profile_detail_url = reverse('profiles:profile_detail')

        return redirect(profile_detail_url)
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

def links(request):
    employees = Profile.objects.all()
    return render(request, 'profiles/links.html', {'employees': employees})
