from django.http import HttpResponse
import feedparser
import ssl
from django.shortcuts import render


# noinspection PyProtectedMember
def index(request):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    # feed = feedparser.parse("https://planetpython.org/rss10.xml")
    feed = feedparser.parse("https://doughellmann.com/blog/feed/")
    context = {
        "entries": feed.entries
    }
    return render(request, "rss.html", context)
