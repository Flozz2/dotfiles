#! /bin/sh

chosen=$(printf "Shutdown\nReboot\nLock" | rofi -dmenu)

case "$chosen" in
    "Shutdown") poweroff ;;
    "Reboot") reboot ;;
    "Lock") slock ;;
    *) exit 1 ;;
esac
