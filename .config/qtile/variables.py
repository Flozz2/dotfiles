# variables.py
mod = "mod4"
alt = "mod1"
terminal = "kitty"
browser = "firefox"
bar_height = 30
default_font = "Ubuntu Mono Nerd Font"

import os
import json


colors = {
    "bg": "#282c34",
    "fg": "#abb2bf",
    "primary": "#61afef",
    "secondary": "#c678dd",
}

wal_colors_path = os.path.expanduser("~/.cache/wal/colors.json")
with open(wal_colors_path, "r") as f:
    wal_colors = json.load(f)

colors["primary"] = wal_colors["colors"]["color1"]
colors["secondary"] = wal_colors["colors"]["color2"]