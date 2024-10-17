from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *


def profile(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')
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

