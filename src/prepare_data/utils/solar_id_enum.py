#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


# Enum for solar data id
@unique
class SolarId(Enum):
    D = "D"  # document
    P = "P"  # paragraph
    S = "S"  # sentence
    W = "W"  # word
