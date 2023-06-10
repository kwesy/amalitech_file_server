# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .models import UserProfile
# from users_profile.forms import UserProfileForm

# # Create your views here.




# @login_required
# def profile(request):
#     user_profile = UserProfile.objects.get(user=request.user)
    
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully.')
#             return redirect('profile')
#     else:
#         form = UserProfileForm(instance=user_profile)
    
#     return render(request, 'account/profile.html', {'form': form})
