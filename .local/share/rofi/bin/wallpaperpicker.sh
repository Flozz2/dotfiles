#! /bin/sh

wallpaperdir="$HOME/Pictures/wallpapers"

chosen=$(ls "$wallpaperdir" | rofi -dmenu)

if [ -n "$chosen" ]; then
    # Update the Qtile config file
    sed -i "s|wallpaper=.*|wallpaper=\"$wallpaperdir/$chosen\",|" ~/.config/qtile/screens.py

    # Reload Qtile
    qtile cmd-obj -o cmd -f restart
fi
