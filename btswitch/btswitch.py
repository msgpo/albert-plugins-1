
""" Extension for controlling the bluetooth adapter """

from albertv0 import *
from shutil import which

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Bluetooth Manager"
__version__ = "0.1"
__trigger__ = "bt"
__author__ = "Simon Krekels"
__dependencies__ = ["rfkill"]

if which("rfkill") is None:
    raise Exception("'rfkill' not found in $PATH.")

def getIcon(arg):
    if arg == "blue":
        return iconLookup("blueman")
    elif arg == "grey":
        return iconLookup("bluetooth-inactive")
    elif arg == "black":
        return iconLookup("bluetooth-black")
    else:
        return iconLookup("blueman")

def handleQuery(query):

    if query.isTriggered:
        items = []
        items.append(Item(
            id = __prettyname__,
            icon = getIcon("blue"),
            text = "Enable Bluetooth",
            subtext = "Enable Bluetooth",
            actions = [
                ProcAction("Enable", ["rfkill", "unblock", "bluetooth"])
                ]))
        items.append(Item(
            id = __prettyname__,
            icon = getIcon("grey"),
            text = "Disable Bluetooth",
            subtext = "Disable Bluetooth",
            actions = [
                ProcAction("Disable", ["rfkill", "block", "bluetooth"])
                ]))
        items.append(Item(
            id = __prettyname__,
            icon = getIcon("black"),
            text = "Manage Devices",
            subtext = "Open Device Manager",
            actions = [
                ProcAction("Open", ["blueman-manager"])
                ]))


        return items
