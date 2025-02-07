# screens.py
from libqtile.config import Screen
from libqtile import bar
from widgets import init_widgets_list, widget_defaults


screens = [
    Screen(
        wallpaper_mode="fill",
        top=bar.Bar(init_widgets_list(), 30, opacity=0.95)),
]
