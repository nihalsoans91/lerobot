import time
from pynput import keyboard

class KeyHandler:
    def __init__(self):
        self.listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release,
        )
        self.listener.start()

    def _on_press(self, key):
        print(f"Pressed: {key}")

    def _on_release(self, key):
        print(f"Released: {key}")

handler = KeyHandler()

# Keep main thread alive
while True:
    time.sleep(1)
