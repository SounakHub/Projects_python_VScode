import random
import os


n = random.randint(0,1)
print(n)

music_dir = 'C:\songs'
song = os.listdir(music_dir)
print(song)

os.startfile(os.path.join(music_dir,song[n]))