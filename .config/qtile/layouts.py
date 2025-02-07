# layouts.py
from libqtile import layout
from variables import colors

# Define a layout theme dictionary
layout_theme = {
    "margin": 10,
    "border_width": 2,
    "border_focus": colors["active_border"],
    "border_normal": colors["inactive_border"],
}

layouts = [
    layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # You can add more layouts if desired:

]
