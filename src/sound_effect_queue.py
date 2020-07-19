import queue

class SoundEffectQueue:
    def __init__(self, directory, num):
        self.q = queue.Queue()
        for i in range(num):
            sfx_file = directory + f'sfx_{i}'
            # sfx = pygame.mixer.music.load(sfx_file)
            self.q.put(sfx_file)

    def play(self):
        sfx = self.q.get()
        sfx.play()
        self.q.put(sfx)
