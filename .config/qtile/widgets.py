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
    # Returns a TextBox with a divider icon.
    # If side is "right", we use the right-pointing arrow ("\ue0b2");
    # if "left", we use the left-pointing arrow ("\ue0b0").
    divider = "\ue0b2" if side == "right" else "\ue0b0" if side == "left" else ''
    return widget.TextBox(
        text=divider,
        padding=0,
        fontsize=bar_height,
        foreground=fg_color,
        background=bg_color,
    )

def separator(color):
    # If the provided color is a key in the colors dictionary, use its value;
    # otherwise, assume the string is already a valid color code.
    color_value = colors[color] if color in colors else color
    return widget.Sep(
        background=color_value,
        foreground=color_value,
        padding=10,
    )

def auto_format_widgets(widgets_list):
    """
    This function performs the following tasks:
      1. Assigns alternating backgrounds to non-spacer widgets.
      2. Inserts left-pointing dividers before each spacer.
      3. Inserts right-pointing dividers after each spacer.
      4. Adds separators and dividers between non-spacer widgets.
    """
    formatted = []
    TRANSPARENT = "#00000000"
    color_cycle = [colors["primary"], colors["secondary"]]
    current_color_index = 0

    # Step 1: Assign backgrounds.
    for w in widgets_list:
        if isinstance(w, widget.Spacer):
            w.background = TRANSPARENT
        else:
            w.background = color_cycle[current_color_index]
            current_color_index = (current_color_index + 1) % len(color_cycle)

    spacer_passed = False
    for i, w in enumerate(widgets_list):
        if isinstance(w, widget.Spacer):
            # Insert a left-pointing divider before the spacer if it's not the first widget.
            if i > 0:
                prev_bg = widgets_list[i - 1].background
                formatted.append(powerline(prev_bg, TRANSPARENT, side="left"))
            formatted.append(w)
            # Insert a right-pointing divider after the spacer if it's not the last widget.
            if i < len(widgets_list) - 1:
                next_bg = widgets_list[i + 1].background
                formatted.append(powerline(next_bg, TRANSPARENT, side="right"))
            spacer_passed = True
        else:
            # For non-spacer widgets, handle separators and dividers.
            if i > 0 and not isinstance(widgets_list[i - 1], widget.Spacer) and spacer_passed:
                prev_bg = widgets_list[i - 1].background
                formatted.append(separator(prev_bg))
                formatted.append(powerline(w.background, prev_bg, side="right"))
            elif i > 0 and not isinstance(widgets_list[i - 1], widget.Spacer) and not spacer_passed:
                prev_bg = widgets_list[i - 1].background
                formatted.append(powerline(prev_bg, w.background, side="left"))
                formatted.append(separator(w.background))                
            formatted.append(w)

    # Append a final separator if the last widget is non-spacer.
    if widgets_list and not isinstance(widgets_list[-1], widget.Spacer):
        last_bg = widgets_list[-1].background
        formatted.append(separator(last_bg))
    return formatted

def init_widgets_list():
    """
    Define your base widgets without specifying backgrounds.
    The auto_format_widgets function assigns alternating backgrounds and
    inserts dividers and separators as specified:
      - Left-pointing dividers before each spacer.
      - Right-pointing dividers after each spacer.
      - Separators and right-pointing dividers between non-spacer widgets.
    """
    base_widgets = [
        widget.GroupBox(
            inactive="000000",
            active="ffffff",
            this_current_screen_border='404040',
            highlight_method='text',
            **widget_defaults,
        ),
        widget.Wttr(
            format="%t(%f) %C",
            **widget_defaults,
        ),
        widget.Spacer(**widget_defaults),
        widget.Memory(
            format="{MemUsed:.1f}{mm}/{MemTotal:.1f}{mm}",
            measure_mem='G',
            **widget_defaults,
        ),
        widget.CPU(
            format='CPU {load_percent}%',
            **widget_defaults
        ),
        widget.CryptoTicker(
            format=" \uf10f: {amount:,.2f}",
            currency="EUR",
            **widget_defaults
        ),
        widget.CheckUpdates(
            distro="Arch_yay",
            no_update_string="Up To Date",
            display_format=" {updates}",
            **widget_defaults
        ),
        widget.Clock(
            format="\uf017  %A %d %B %H:%M",
            **widget_defaults
        ),
        widget.TextBox(
            text="\u23FB",
            mouse_callbacks={"Button1": lazy.spawn(os.path.expanduser("~/.local/share/rofi/bin/powermenu.sh"))},
            fontsize=16,
            font=default_font,
            margin=10,
            padding=10,
        ),
    ]
    return auto_format_widgets(base_widgets)
