import json
def load_settings():
    settings = open("settings.json", "r", encoding="utf8")
    settings = json.loads(settings.read())
    sKeyMap = settings["keymap"]
    return settings["keymap_options"][sKeyMap]


def save_settings():
    ...
