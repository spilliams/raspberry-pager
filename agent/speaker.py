import numpy
import sounddevice
import wave


class Speaker:
    def __init__(self, samplerate=44100):
        self._wave = None
        self._out_stream = sounddevice.OutputStream(
            device="default",
            dtype="int16",
            channels=2,
            samplerate=samplerate
            callback=self.audio_playback_callback,
        )

    def play_clip(self, filename="7.wav"):
        self._read_wav_file(filename)
        self._out_stream.start()

    def _read_wav_file(self, filename):
        self._wave_read = wave.open(filename, "r")
        self._written = self._wave_read.getnframes()

    def audio_playback_callback(self, outdata, frames, time, status):
        raw_data = self._wave_read.readframes(frames)
        outframes = len(raw_data) // 4
        data = numpy.frombuffer(raw_data, dtype="int16")
        outdata[:][:outframes] = data.reshape((outframes, 2))

        if outframes < frames:
            # self._playback_stopped()
            raise sounddevice.CallbackStop


if __name__ == "__main__":
    s = Speaker()
    s.play_clip()
