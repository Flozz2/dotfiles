# hooks.py
import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    exec_path = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(exec_path)

