from pystray import Icon, Menu, MenuItem
from PIL import Image

from open_local_location import open_explorer


def quit_app():
    app.stop()


def run_app():
    pass


image = Image.open('open_local_location/icon.png')
menu = Menu(MenuItem('Quit', quit_app), MenuItem('Run', run_app))
app = Icon(name='test', icon=image, title='pystray App', menu=menu)
app.run()

open_explorer('Syntegrate&vicc Dropbox')
