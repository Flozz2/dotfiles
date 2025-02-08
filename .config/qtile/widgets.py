# widgets.py
from libqtile import widget
from libqtile.lazy import lazy
import os

from variables import colors, bar_height, default_font


# Widget default settings
widget_defaults = dict(
    font=default_font,
    fontsize=16,
    padding=3,

)


def powerline(fg_color, bg_color=None, side="right"):
    return widget.TextBox(
        text="\ue0b2" if side == "right" else "\ue0b0" if side == "left" else '',  # nf-pl-right_hard_divider
        padding=0,
        fontsize=bar_height,
        foreground=fg_color,
        background=bg_color
    )

def separator(color):
    return widget.Sep(
            background=colors[color],
            foreground=colors[color],
            padding=10,
    )

def init_widgets_list():
    return [
        widget.GroupBox(
            inactive="000000",
            active="ffffff",
            this_current_screen_border='404040',
            highlight_method='text',
            background=colors["primary"],
            **widget_defaults,
        ),
        powerline(colors["primary"], colors["bg"], side="left"),
        widget.Spacer(
            background=colors["bg"],
            **widget_defaults),
        powerline(colors["primary"], colors["bg"]),
        widget.Systray(
            background=colors["primary"],
            **widget_defaults
        ),
        separator("primary"),
        powerline(colors["secondary"], colors["primary"]),
        widget.CryptoTicker(
            format=" \uf10f: {amount:,.2f}",  # nf-fa-money
            currency="EUR",
            background=colors["secondary"],
            **widget_defaults
        ),
        separator("secondary"),
        powerline(colors["primary"], colors["secondary"]),
        widget.CheckUpdates(
            distro="Arch_yay",
            no_update_string="Up To Date",
            display_format=" {updates}",  # nf-fa-download
            background=colors["primary"],
            **widget_defaults
        ),
        separator("primary"),
        powerline(colors["secondary"], colors["primary"]),
        widget.Clock(
            format="\uf017  %A %d %B %H:%M",  # nf-fa-clock_o
            background=colors["secondary"],
            **widget_defaults
        ),
        separator("secondary"),
        powerline(colors["primary"], colors["secondary"]),
        widget.TextBox(
            text="\u23FB",  # nf-fa-power_off
            mouse_callbacks={"Button1": lazy.spawn(os.path.expanduser("~/.local/share/rofi/bin/powermenu.sh"))},
            fontsize=16,
            font=default_font,
            margin=10,
            padding=10,
            background=colors["primary"],
        ),
        separator("primary"),
    ]