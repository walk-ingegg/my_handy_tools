import os
import json
import glob
import pyperclip
import subprocess
from tkinter import messagebox

filepath = pyperclip.paste()
filepath = filepath.strip('"')


def get_dir():
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
        return json_["business"]["root_path"]
    else:
        messagebox.showwarning("ERROR", "failed to find info.json")
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
        messagebox.showwarning("ERROR", "failed to get local path")
        pass


def open_dir(path):
    # 対象がファイルだった場合、ベースネーム（フォルダパス）を取得
    if os.path.isfile(path):
        path = os.path.dirname(path)

    subprocess.Popen(['explorer', path])


if not "Syntegrate&vicc Dropbox" in filepath:
    messagebox.showwarning("ERROR", "No Dropbox path in clipboard")
    pass
else:
    mydir = get_dir()
    local = get_local_path(filepath, mydir)
    open_dir(local)
