from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profiles
from django.contrib.auth.models import User


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profiles.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


def profile_deleted(sender, instance, **kwargs):
    if instance:
        user = instance.user
        user.delete()


post_save.connect(create_user_profile, sender=User)
post_delete.connect(profile_deleted, sender=Profiles)