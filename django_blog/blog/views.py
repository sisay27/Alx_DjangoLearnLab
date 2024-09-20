from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    user = request.user
    if request.method == 'POST':
        user.email = request.POST.get('email')
        # Update other profile fields as needed
        user.save()
        # Redirect to the profile page or a success page
        return redirect('profile')
    context = {
        'user': user
    }
    return render(request, 'app_name/profile.html', context)