#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


# Enum for solar data
@unique
class Solar(Enum):
    COMPLETE = "COMPLETE"  # complete solar data (source + target + link)
    SOURCE = "SOURCE"
    TARGET = "TARGET"
    LINK = "LINK"
