from rest_framework import generics

from songs.serializers import SongSerializer

from .models import Song


class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
