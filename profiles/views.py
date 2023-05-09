from django.shortcuts import render
from .models import Profile

def profile_detail(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # Process form submission
        # Update the profile with the form data
        profile.phone_number = request.POST['phone_number']
        profile.address = request.POST['address']
        profile.save()
        return redirect('profiles:profile_detail')
    else:
        return render(request, 'profiles/edit_profile.html', {'profile': profile})
