import pygame
import queue

class SoundEffectQueue:
    def __init__(self, directory, prefix, num):
        self.q = queue.Queue()
        for i in range(num):
            sfx_file = directory + f'{prefix}_{i}.mp3'
            self.q.put(sfx_file)

    def play(self):
        sfx_file = self.q.get()
        pygame.mixer.music.load(sfx_file)
        pygame.mixer.music.play(loops=0)
        self.q.put(sfx_file)
