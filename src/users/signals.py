from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender = User) ## When a user is saved then send this signal
    ## and this signal is going to be received by this decorator and it's gonna wrap the 
    ## create_profile function receive all the parameters that our post_save signal past to it
def create_profile(sender, instance, created, **kwargs):
    if created :
        Profile.objects.create(user = instance) ##create a profile object of that instance

@receiver(post_save, sender = User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()
