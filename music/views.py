from django.shortcuts import render
from  django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the music homepage.</h1>")

# Create your views here.
def detail(request, album_id):
    return HttpResponse('<h2>Details for Album id : ' + str(album_id) + '</h2>')
