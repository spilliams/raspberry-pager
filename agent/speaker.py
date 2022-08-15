import numpy
import sounddevice
import wave


class Speaker:
    def __init__(self):
        self._vu_left = 0
        self._vu_right = 0
        self._graph = [0 for _ in range(44)]
        self._wave = None
        self._out_stream = sounddevice.OutputStream(
            device="default",
            dtype="int16",
            channels=2,
            samplerate=22000,
            callback=self.audio_playback_callback,
        )

    def play_clip(self, filename="weow.wav"):
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

        self._vu_left = numpy.average(numpy.abs(outdata[:, 0])) / 65535.0 * 10
        self._vu_right = numpy.average(numpy.abs(outdata[:, 1])) / 65535.0 * 10
        self._graph.append(min(1.0, max(self._vu_left, self._vu_right)))
        self._graph = self._graph[-44:]

        if outframes < frames:
            # self._playback_stopped()
            raise sounddevice.CallbackStop


if __name__ == "__main__":
    s = Speaker()
    s.play_clip()
