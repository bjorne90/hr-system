from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string

class WorkShift(models.Model):
    name = models.CharField(max_length=100, default='Location')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    role = models.CharField(max_length=100, blank=True)
    is_booked = models.BooleanField(default=False)

    def get_current_time(self):
        return timezone.now()
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workshift = models.ForeignKey(WorkShift, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return f"Booking: {self.user} - {self.workshift}"

@login_required
def workshift_list(request):
    from .models import WorkShift
    workshifts = WorkShift.objects.exclude(booking__isnull=False)
    return render(request, 'scheduling/workshift_list.html', {'workshifts': workshifts})

@login_required
def book_workshift(request, workshift_id):
    workshift = get_object_or_404(WorkShift, id=workshift_id)

    if workshift.start_time > timezone.now():
        if request.method == 'POST':
            # Handle the booking logic
            # ...

            # Update the user's profile with the booked workshift
            user_profile = request.user.profile
            user_profile.booked_workshifts.add(workshift)
            user_profile.save()

            # Render a success message
            success_message = 'Du är bokad på detta pass.'
            return render(request, 'scheduling/book_workshift.html', {'workshift': workshift, 'success_message': success_message})

        return render(request, 'scheduling/book_workshift.html', {'workshift': workshift})
    else:
        error_message = 'Detta pass har redan passerat och kan inte bokas.'
        return render(request, 'scheduling/book_workshift.html', {'workshift': workshift, 'error_message': error_message})


@login_required
def work_shifts(request):
    from booking.models import Booking
    user_profile = request.user.profile
    booked_workshifts = Booking.objects.filter(user=user_profile)
    return render(request, 'scheduling/work_shifts.html', {'booked_workshifts': booked_workshifts})

@login_required
def add_event(request):
    # Handle adding event logic
    return render(request, 'scheduling/add_event.html')



@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, created, **kwargs):
    if created:  # Check if a new booking record was created
        # Send an email to the user
        subject = 'Shift Booking Confirmation'
        message = 'You have been booked for a new shift.'
        email_from = settings.DEFAULT_FROM_EMAIL  # Replace with your own email
        recipient_list = [instance.user.email]  # Send email to user

        html_message = render_to_string('email/booking_confirmation.html', {'booking': instance})
        send_mail(subject, message, email_from, recipient_list, html_message=html_message, fail_silently=False)