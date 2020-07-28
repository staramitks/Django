# Custom created file
from django.http import HttpResponse
import GetOldTweets3 as got
from django.shortcuts import render

def index(request):
    params = {'name': 'Amit Singh', 'location': 'Agra'}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("Hello About Django")

def removepunc( request ):
    djtext = request.GET.get('text','default')
    print (djtext)
    return HttpResponse("Punc removed")

def tweets(request):
    tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama") \
        .setTopTweets(True) \
        .setMaxTweets(10)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    for x in range(len(tweet)):
        print(tweet[x].text)
    return HttpResponse(tweet[x].text)
