import os
import json
import glob
import pyperclip
import subprocess

filepath = pyperclip.paste()
filepath = filepath.strip('"')


def getDir():
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
        print("failed to find info.json")
        pass


def getLocalPath(path, dirpath):
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
        print("failed to get local path")
        pass


def open_dir(path):
    # 対象がファイルだった場合、ベースネーム（フォルダパス）を取得
    if os.path.isfile(path):
        path = os.path.dirname(path)

    subprocess.Popen(['explorer', path])


if not "Dropbox" in filepath:
    pass
else:
    mydir = getDir()
    local = getLocalPath(filepath, mydir)
    open_dir(local)
