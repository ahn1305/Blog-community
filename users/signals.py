from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# we have a sender, and a signal post_save, so when a user is saved send this signal and this is going to
# be received by the receiver is the create_profile, takes all of this arguements that our post_save signal,
# passed to it and one of those is the instance of the user and created, if created then create,
# a profile object.

# kwargs, it accepts any key word arguements
# instance is the user

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save() # save the profile


"""
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)


We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.


https://www.geeksforgeeks.org/args-kwargs-python/


"""