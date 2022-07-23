import json

config_file = "open_local_location\config\config.json"


def set_config(key):
    config_data = {"hotkey": key}

    with open(config_file, "w") as f:
        json.dump(config_data, f)


def load_config():
    with open(config_file, "r") as f:
        tmp = json.load(f)
    
    return tmp["hotkey"]


if __name__ == "__main__":
    set_config("ctrl+shift+a")
    key_config = load_config()
    print(key_config)