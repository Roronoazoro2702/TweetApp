from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm

def home(request):
    return render(request, 'tweets/home.html')

@login_required
def tweet_list(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'form': form, 'tweets': tweets})

