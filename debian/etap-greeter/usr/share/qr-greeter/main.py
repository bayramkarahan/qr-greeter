#!/usr/bin/python3
import os
import sys
import subprocess

if os.getuid() != 0:
    print("Permission denied",file=sys.stderr)
    sys.exit(1)

os.system("""
xset s off || true
xset dpms 0 0 0 || true
xset -dpms s off || true
xset s noblank || true
""")

if not os.path.isdir("module"):
    os.chdir("/usr/share/qr-greeter")

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

from util import *

os.environ["UBUNTU_MENUPROXY"]=""
os.environ["GDK_CORE_DEVICE_EVENTS"]="1"
os.environ["GTK_THEME"]="Adwaita-dark"
os.system("xhost +localhost")

os.umask(0o077)

loaded_modules = []
for module in ["lightdm.py", "gtkwindow.py"] + os.listdir("module"):
    if module in loaded_modules:
        continue
    if not os.path.isfile("module/{}".format(module)):
        continue
    with open("module/{}".format(module),"r") as f:
        exec(f.read())
        module_init()
        del(module_init)
        loaded_modules.append(module)

os.chdir(os.environ["HOME"])
settings = Gtk.Settings.get_default()
settings.set_property('gtk-application-prefer-dark-theme', True)
settings.set_property('gtk-theme-name','Adwaita-dark')

Gtk.main()
