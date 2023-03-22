#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def get_logger(logger_name):
    """
    Creates a logger with the given name.

    @param logger_name: name of the logger
    @return: logger
    """
    # Config logger
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - {}: %(message)s".format(logger_name),
        level=logging.INFO,
        datefmt="%d-%b-%y %H:%M:%S",
    )

    logger = logging.getLogger()
    return logger
