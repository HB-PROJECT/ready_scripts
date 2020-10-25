text = """
+------------+---------------------------------------------+
|  Commands  |                    Usage                    |
+------------+---------------------------------------------+
|  CTRL + C  | copy to your clipboard from other resources |
| CTRL + ALT |         to paste to dl.iitu browser         |
+------------+---------------------------------------------+
"""


from tkinter import Tk
from pynput import keyboard
from pynput.keyboard import Controller
controller = Controller()

print('\nSPECIAL FOR IITU STUDENTS 😉\n')
print('Sites like dl.iitu does not allow commands like CTRL+V')
print('This script uses the command CTRL+ALT instead of CTRL+V to paste')
print(text)


def on_activate():
    text = Tk().clipboard_get()
    for i in text:
        controller.type(i)


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>'),on_activate)
with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
    l.join()
