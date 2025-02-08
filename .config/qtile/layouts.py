# layouts.py
from libqtile import layout
from variables import colors

# Define a layout theme dictionary
layout_theme = {
    "margin": 8,
    "border_width": 2,
    "border_focus": colors["primary"],
    "border_normal": colors["bg"],
}

layouts = [
    layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # You can add more layouts if desired:

]
