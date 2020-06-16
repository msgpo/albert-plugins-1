
"""This extension activates the buienradar GIF generator"""

import os
import subprocess
from shutil import which
from albertv0 import *


__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Buienradar plugin"
__version__ = "0.1"
__trigger__ = "radar"
__author__ = "Simon Krekels"
__dependencies__ = ["radar"]

if which("radar") is None:
    raise Exception("'radar' not found in $PATH.")

def getIcon():
   return "/home/simon/git/Buienradar/logo-kmi--nl.png"

def handleQuery(query):

    if query.isTriggered:
        items = []
        items.append(Item(id = __prettyname__,
               icon = getIcon(),
               text = "Buienradar",
               subtext = "Show buienradar for past 90 minutes",
               actions = [
                   ProcAction("Buienradar", ["radar"])
                   ]))
    return items

