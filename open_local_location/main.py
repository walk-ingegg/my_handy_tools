import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image
import keyboard
import pyperclip

from open_local_location import open_explorer


def open_main():
    file_path = pyperclip.paste()
    file_path = file_path.strip('"')
    open_explorer('business', file_path)


def quit_app():
    global app
    app.stop()


def run_app():
    global app

    menu = Menu(MenuItem('Quit', quit_app))
    image = Image.open('open_local_location/icon.png')
    app = Icon("name", image, "Dropen", menu)
    app.run()


def main():
    threading.Thread(target=run_app).start()

    keyboard.add_hotkey("ctrl+alt+p", open_main)


if __name__ == "__main__":
    main()
