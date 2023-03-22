#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


# Enum for Lektor data
@unique
class Lektor(Enum):
    COMPLETE = "COMPLETE"  # complete Lektor data (source + target)
    SOURCE = "SOURCE"
    TARGET = "TARGET"
