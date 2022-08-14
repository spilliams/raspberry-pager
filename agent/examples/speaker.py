# import sounddevice


# def play_clip(filename="WEEEOOOOWW.mp3"):
#     out_device = "default"
#     out_stream = sounddevice.OutputStream(
#         device=out_device,
#         dtype="int16",
#         channels=2,
#         samplerate=16000,
#         callback=self.audio_playback_callback,
#     )

#     out_stream.start()


# if __name__ == "__main__":
#     play_clip()


import pygame

path = "/home/pi/pager/source/agent/examples/WEEEOOOOWW.mp3"
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.load(path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
