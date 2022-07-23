import os
import json
import glob
import subprocess
from tkinter import messagebox, Tk
from urllib.request import OpenerDirector


def show_message(title, message):
    root = Tk()
    root.geometry('300x300')
    root.attributes('-topmost', True)
    root.withdraw()

    messagebox.showwarning(title, message)


def get_dir(account):
    # get path to Dropbox directory
    info = "\Dropbox\info.json"
    env = ["APPDATA", "LOCALAPPDATA"]
    json_ = None

    for v in env:
        j = glob.glob(os.getenv(v)+info)
        if j:
            json_ = json.load(open(j[0]))
            break

    if json_ != None:
        return json_[account]["root_path"]
    else:
        show_message("ERROR", "failed to find info.json")
        pass


def get_local_path(path, dirpath):
    if path and dirpath:
        ps = path.split("\\")
        pss = []
        pd = dirpath.split("\\")
        dir = pd[len(pd)-1]

        depth = ps.index(dir)
        for n in range(depth+1, len(ps)):
            pss.append(ps[n])

        path_ = dirpath + "\\" + "\\".join(pss)
        return path_

    else:
        show_message("ERROR", "failed to get local path")
        pass


def open_dir(path):
    # 対象がファイルだった場合、ベースネーム（フォルダパス）を取得
    if os.path.isfile(path):
        path = os.path.dirname(path)

    subprocess.Popen(['explorer', path], shell=False)


def open_explorer(account_type, file_path):
    mydir = get_dir(account_type)
    name = mydir.split("\\")
    path = name[len(name)-1]
    if path in file_path:
        local = get_local_path(file_path, mydir)
        open_dir(local)
    else:
        show_message("ERROR", "No Dropbox path in clipboard")
        pass


# import pyperclip
# file_path = pyperclip.paste()
# file_path = file_path.strip('"')
# open_explorer('business', file_path)
