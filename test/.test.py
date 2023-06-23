import keyboard
from playsound import playsound

def on_press_key(event):
    print("yo")

def on_release_key(event):
    playsound("voice.wav")

# Register the event handlers
keybind = "a"
keyboard.on_press_key(keybind, on_press_key)
keyboard.on_release_key(keybind, on_release_key)

# Keep the program running until interrupted
keyboard.wait()