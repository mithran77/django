from .models import Album, Song
from django.shortcuts import render, get_object_or_404

def index(request):
    # 
    context = { 'all_albums' : Album.objects.all() }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', { 'album' : album })

def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album' : album ,
            'error_message' : 'You did not select a valid Song',
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', { 'album' : album })
