from django.shortcuts import render, redirect
from .models import UserProfile
from .models import *

def view_profile(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    return render(request, 'profiles/profile.html', {'user_profile': user_profile})


# @login_required
def follow_user(request, username):
    user_to_follow = User.objects.get(username=username)
    request.user.userprofile.following.add(user_to_follow)
    return redirect('view_profile', username=username)

# @login_required
def unfollow_user(request, username):
    user_to_unfollow = User.objects.get(username=username)
    request.user.userprofile.following.remove(user_to_unfollow)
    return redirect('view_profile', username=username)

def view_notifications(request):
    notifications = Notification.objects.filter(user=request.user, read=False)
    return render(request, 'notifications/notifications.html', {'notifications': notifications})

def like_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    review.likes.add(request.user)
    return redirect('view_review', review_id=review_id)