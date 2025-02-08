# screens.py
from libqtile.config import Screen
from libqtile import bar
from widgets import init_widgets_list, widget_defaults

from variables import bar_height

screens = [
    Screen(
        wallpaper_mode="fill",
        top=bar.Bar(init_widgets_list(), bar_height, opacity=1)),
]
