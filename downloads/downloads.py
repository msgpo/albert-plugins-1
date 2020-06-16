# -*- coding: utf-8 -*-

"""This is a simple trash extension providing a single item which opens the systems downloads \
location in your default file manager on activation."""

import re

from albertv0 import *

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Downloads"
__version__ = "1.0"
__trigger__ = "downloads "
__author__ = "Simon Krekels"
__dependencies__ = []

iconPath = iconLookup("blue-folder-download")


def handleQuery(query):

    if query.string.strip() and "downloads".startswith(query.string.lower()):
        pattern = re.compile(query.string, re.IGNORECASE)
        return Item(
            id="downloads-open",
            icon=iconPath,
            text=pattern.sub(lambda m: "<u>%s</u>" % m.group(0), "Downloads"),
            subtext="Show downloads folder",
            completion="downloads",
            actions=[UrlAction("Show", "~/Downloads")]
        )
