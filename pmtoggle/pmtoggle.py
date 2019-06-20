
"""This extension toggles xfce Presentation Mode"""

import os
import subprocess
from shutil import which
from albertv0 import *


__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Presentation Mode Toggle"
__version__ = "0.1"
__trigger__ = "pm"
__author__ = "Simon Krekels"
__dependencies__ = ["pmtoggle"]

if which("pmtoggle") is None:
    raise Exception("'pmtoggle' not found in $PATH.")

def getIcon(arg):
    if arg == "toggle":
        return iconLookup("monitor")
    elif arg == True:
        return iconLookup("checkmark")
    elif arg == False:
        return iconLookup("emblem-noread")
    else:
        return iconLookup("monitor")

def isActive():
    var = subprocess.check_output(["xfconf-query",
        "-c", "xfce4-power-manager",
        "-p", "/xfce4-power-manager/presentation-mode"])[:-1]
    if var == b'true':
        return True 
    else:
        return False


def handleQuery(query):

    if query.isTriggered:
        items = []
        items.append(Item(id = __prettyname__,
               icon = getIcon("toggle"),
               text = "Presentation Mode Toggle",
               subtext = "Toggle xfce Presentation Mode",
               actions = [
                   ProcAction("Toggle", ["pmtoggle"])
                   ]))
        items.append(Item(id=__prettyname__,
               text = "Currently Active: {}".format(isActive()),
               icon = getIcon(isActive()) 
               ))
        return items

