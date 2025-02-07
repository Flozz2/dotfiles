# widgets.py
from libqtile import widget
from libqtile.lazy import lazy

import os

# Widget default settings
widget_defaults = dict(
    font="Ubuntu Mono Nerd Font",
    fontsize=16,
    padding=3,
)

def init_widgets_list():
    return [
        widget.GroupBox(**widget_defaults),
        widget.Prompt(**widget_defaults),
        widget.WindowName(**widget_defaults),
        widget.Systray(**widget_defaults),
        #widget.Net(interface="wlp6s0", **widget_defaults),
        widget.CheckUpdates(distro="Arch_yay", no_update_string="", **widget_defaults),
        widget.Clock(format="%a %d %b %Y %H:%M", **widget_defaults),
        widget.TextBox("\u23FB", mouse_callbacks={"Button1" : lazy.spawn(os.path.expanduser("~/.local/share/rofi/bin/powermenu.sh"))}, fontsize=16, font="Ubuntu Mono Nerd Font", margin=10, padding=10)
        # … add additional widgets as desired
    ]
