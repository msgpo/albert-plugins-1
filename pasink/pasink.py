
""" Module to set default PulseAudio sink from Albert """

import os
import subprocess
from shutil import which
from albertv0 import *
import re

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Pulse Audio Sink"
__version__ = "0.1"
__trigger__ = "sink"
__author__ = "Simon Krekels"
__dependencies__ = ["pulseaudio"]

if which("pacmd") is None:
    raise Exception("'pacmd' not found in $PATH. Is PulseAudio installed?")


class Sink():

    def __init__(self, name, index, icon):
        self.name = name
        self.index = index
        self.icon = icon

    def getName(self):
        return self.name

    def getIndex(self):
        return self.index

    def getIcon(self):
        return self.icon


def getSinks():
    var = subprocess.check_output(["pacmd", "list-sinks"]).decode("utf-8")
    var2 = var.split("\n")
    indices = []
    for item in var2:
        items = item.split()
        if "index:" in items:
            indices.append(items[-1])

    devices = var.split("index:")[1:]
    sinks = []
    quoted = re.compile('"[^"]*"')

    for i in range(len(devices)):
        for item in devices[i].split("\n"):
            index = indices[i]
            items = item.split()
            if "device.description" in items:
                name = quoted.findall(item)[0].strip('"')
            if "device.icon_name" in items:
                icon = quoted.findall(item)[0].strip('"')
                if "bluetooth" in icon:
                    icon = "blueman-device"
        sinks.append(Sink(name,index,icon))
    return sinks
    

def handleQuery(query):

    if query.isTriggered:
        sinks = getSinks()
        items = []
        for sink in sinks:
           items.append(Item(id = __prettyname__,
               text = sink.getName(),
               subtext = "Set default sink to <u>{}</u>".format(sink.getName()) ,
               icon = iconLookup(sink.getIcon()),
               actions = [
                   ProcAction("Set as default", ["pacmd", "set-default-sink", sink.getIndex()])
                   ]))
        return items

