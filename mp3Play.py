from pygame import mixer

mixer.init()
mixer.music.load('mp3Play.mp3')
mixer.music.play()
input('Agora você escuta?')
