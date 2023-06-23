from playsound import playsound
import keyboard
import pyaudio
import wave



KEYBIND_TALK = "a"
chunk = 1024  # Record in chunks of 1024 samplesaaaaaaaaaaaaaaaaaa
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
filename = "sound/output.wav"


#On keybind press, records voice while held.
def on_press_key(event):
    print("recording")
    global frames, stream, recording
    if not recording:
        recording = True
        frames = []
        stream = pa.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

#on release of keybind, saves the sound and converts to wav file.
def on_release_key(event):
    global recording, stream
    recording = False
    stream.stop_stream()
    stream.close()
    stream = None


    #saves to wav file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pa.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("Completed voice recording")


    #pass audio to translator and to AIVoice output, then play sound.


if __name__ == "__main__":

    #Event handlers which perform when the KEYBIND_TALK key is pressed
    keyboard.on_press_key(KEYBIND_TALK, on_press_key)
    keyboard.on_release_key(KEYBIND_TALK, on_release_key)
    
    # Store the frames in an array
    frames = []
    recording = False
    stream = None
    
    #Create portAudio interface
    pa = pyaudio.PyAudio()

    try:
        while True:
            if(recording and stream is not None):
                data = stream.read(chunk)
                frames.append(data)



    except KeyboardInterrupt as e:
        print("Stopped voice record due to " + str(e))

    except Exception as e:
        print("an error occured: " + str(e))
        pass
        
