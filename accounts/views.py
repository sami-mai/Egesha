from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from accounts.models import 
# from . import forms


@login_required
def edit_profile(request, username):
    current_user = request.user
    # profile = Profile.objects.get(user=current_user.id)
    # if request.method == 'POST':
    #     profile_form = forms.EditProfile(request.POST, request.FILES, instance=current_user.profile)
    #     user_form = forms.EditUserForm(request.POST, instance=current_user)
    #     if profile_form.is_valid() and user_form.is_valid():
    #         profile = profile_form.save(commit=False)
    #         user = user_form.save(commit=False)
    #         profile.user = current_user
    #         profile.save()
    #         user.save()
    #         return redirect('user_profile', current_user.id)
    # else:
    #     profile_form = forms.EditProfile()
    #     user_form = forms.EditUserForm()
    context = {
        "current_user": current_user,
        # "profile": profile,
        # "profile_form": profile_form,
        # "user_form": user_form,
    }
    return render(request, 'accounts/edit_profile.html', context)


# @login_required
# def dashboard(request, username):
#     current_user = request.user
#     profile = Profile.objects.get(user=current_user.id)
#     context = {
#         "current_user": current_user,
#         "profile": profile
#     }
#     return render(request, 'accounts/dashboard.html', context)
