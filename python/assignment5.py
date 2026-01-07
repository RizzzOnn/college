import random
from collections import deque

# Track class
class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.length = random.randint(5, 10)

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.length} min)"


# Playlist using Queue
class Playlist:
    def __init__(self):
        self.queue = deque()

    # Add song (enqueue)
    def add_song(self, track):
        self.queue.append(track)
        print("Added:", track)

    # Play next song (dequeue)
    def play_song(self):
        if self.queue:
            current = self.queue.popleft()
            print("Now Playing:", current)
        else:
            print("Playlist is empty!")

    # Show current song
    def show_current(self):
        if self.queue:
            print("Next Song:", self.queue[0])
        else:
            print("No song in playlist!")


# Main program
playlist = Playlist()

# Creating tracks
song1 = Track("Shape of You", "Ed Sheeran")
song2 = Track("Blinding Lights", "The Weeknd")
song3 = Track("Believer", "Imagine Dragons")

# Adding songs
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)

print()

# Playing songs
playlist.show_current()
playlist.play_song()
playlist.show_current()
playlist.play_song()
playlist.play_song()
playlist.play_song()
