import threading
import time
from pystray import Icon, Menu, MenuItem
from PIL import Image
import keyboard
import pyperclip

from open_local_location import open_explorer


def open_main():
    file_path = pyperclip.paste()
    file_path = file_path.strip('"')
    time.sleep(1)
    open_explorer('business', file_path)


def quit_app():
    global app
    app.stop()


def set_shortcut():
    print('hoge')


def run_app():
    global app

    menu = Menu(MenuItem('Quit', quit_app), MenuItem('Shortcut', set_shortcut))
    image = Image.open('open_local_location\config\Dropen.ico')
    app = Icon("name", image, "Dropen", menu)
    app.run()


def main():
    threading.Thread(target=run_app).start()

    keyboard.add_hotkey("ctrl+shift+a", open_main)


if __name__ == "__main__":
    main()
