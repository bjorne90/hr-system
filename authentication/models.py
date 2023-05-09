from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from booking.models import Booking
from profiles.models import Profile

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auth_profile')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    booked_workshifts = models.ManyToManyField(Booking, related_name='booked_users')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            instance.auth_profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'auth_profile'):
        instance.auth_profile.save()
