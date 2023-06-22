from playsound import playsound
import keyboard
import pyaudio
import wave



KEYBIND_TALK = "a"
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
filename = "output.wav"


#On keybind press, records voice while held.
def on_press(event):
    global frames, stream, pa, recording
    recording = True
    stream = pa.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

#on release of keybind, saves the sound and converts to wav file.
def on_release(event):
    playsound("voice.wav")
    global recording
    stream.stop_stream()
    stream.close()
    recording = False

    #saves to wav file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pa.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


    #pass audio to translator and to AIVoice output, then play sound.


if __name__ == "__main__":
    #Create portAudio interface
    pa = pyaudio.PyAudio()

    # Store the frames in an array
    frames = []
    stream = None
    recording = False
    
    keyboard.on_press(KEYBIND_TALK, on_press)
    keyboard.on_release(KEYBIND_TALK, on_release)

try:
    #creates an inf loop
    while True:
        if(recording == True):
            data = stream.read(chunk)
            frames.append(data)
except KeyboardInterrupt:
    print("Recording state off.")
        
