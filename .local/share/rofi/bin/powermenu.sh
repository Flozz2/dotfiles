#! /bin/sh

chosen=$(printf "Shutdown\nReboot\nLock" | rofi -dmenu)

case "$chosen" in
    "Shutdown") poweroff ;;
    "Reboot") reboot ;;
    "Lock") dm-tool lock ;;
    *) exit 1 ;;
esac
