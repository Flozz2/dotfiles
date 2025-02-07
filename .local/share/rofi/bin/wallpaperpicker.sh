#! /bin/sh

wallpaperdir="$HOME/Pictures/wallpapers"

# Present the list of wallpapers using rofi and capture the chosen filename.
chosen=$(ls "$wallpaperdir" | rofi -dmenu)

if [ -n "$chosen" ]; then
    wallpaper_path="$wallpaperdir/$chosen"
    # Use feh to set the wallpaper (scaling the image to fill the screen).
    feh --bg-scale "$wallpaper_path"
fi
