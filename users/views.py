from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *


def profile(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile':profile})

@login_required
def profile_edit(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    if request.path == reverse('onboarding'):
        onboarding = True
    else:
        onboarding = False
    profile = request.user.profile
    form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_edit.html', {'form':form, 'profile':profile, 'onboarding':onboarding,})

