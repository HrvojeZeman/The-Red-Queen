import sounddevice as sd
import numpy as np
import keyboard
import scipy.io.wavfile

sample_rate = 16000
channels = 1
dtype = 'int16'
recorded_frames = []

print("Hold ctrl to record...")

try:
    while True:
        if keyboard.is_pressed('ctrl'):
            print("Recording... (release to stop)")
            recorded_frames = []
            with sd.InputStream(samplerate=sample_rate, channels=channels, dtype=dtype) as stream:
                while keyboard.is_pressed('ctrl'):
                    audio_chunk, _ = stream.read(1024)
                    recorded_frames.append(audio_chunk)
            print("Recording stopped.")
            
            audio_data = np.concatenate(recorded_frames, axis=0) # TODO: add audio chunk processing instead of files
            scipy.io.wavfile.write("recorded_output.wav", sample_rate, audio_data)
            print("Saved to recorded_output.wav")
        else:
            sd.sleep(100)  # prevent CPU overuse

except KeyboardInterrupt:
    print("\nExiting...")