import sounddevice


def play_clip(filename="WEEEOOOOWW.mp3"):
    out_device = "default"
    out_stream = sounddevice.OutputStream(
        device=out_device,
        dtype="int16",
        channels=2,
        samplerate=16000,
        callback=self.audio_playback_callback,
    )

    out_stream.start()


if __name__ == "__main__":
    play_clip()
