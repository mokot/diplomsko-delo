#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


def read_xml(file_name):
    """
    Reads an XML file and returns the root element.

    @param file_name: name of the XML file
    @return: root element of the XML file
    """
    # Pass the path of the xml document to enable the parsing process
    element_tree = ET.parse(file_name)

    # Get the parent tag of the xml document
    root = element_tree.getroot()

    # Return the root tag of the xml document, along with its memory location
    return root
