from django.shortcuts import render
from django.http import JsonResponse
from .models import Album 
def add_album(request):
    Album.objects.create(
        title = request.GET.get("title"),
        artist = request.GET.get("artist"),
        cover_art = request.GET.get("cover_art"),
        release_year = request.GET.get("release_year"),
        genre = request.GET.get("genre")
    )
    return JsonResponse({"status": "ok"})

def load_album(request):
    requested_album = Album.objects.filter(artist=request.GET.get("artist")).filter(title=request.GET.get("title"))
    if(not requested_album):
        return JsonResponse({"status": "album not found"})
    return JsonResponse({
        "artist": requested_album[0].artist,
        "title": requested_album[0].title,
        "cover_art": requested_album[0].cover_art,
        "release_year": requested_album[0].release_year,
        "genre": requested_album[0].genre
        })