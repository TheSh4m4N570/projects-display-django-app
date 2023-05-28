from django.shortcuts import render
from .models import Profiles


# Profile page
def profiles(request):
    profiles = Profiles.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def profile(request, username):
    profile = Profiles.objects.get(username=username)
    topskills = profile.skill_set.exclude(description__exact="")
    otherskills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topskills': topskills, 'otherskills': otherskills}
    return render(request, 'users/profile.html', context)
