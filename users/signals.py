# signal that gets fired when an object is saved
from django.db.models.signals import post_save
# Sender
from django.contrib.auth.models import User
# Receiver
from django.dispatch import receiver
from .models import Profile

# We want a user profile to be created for all new users.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
