#!/usr/bin/env python3

import loggz

from loadguard.runners import ProjectStore

LOG = loggz.factory('transilien.louvre_piv.push')
""" The main logger. """


def run(store: ProjectStore):
    """ LoadGuard Task entry point.
    """
    return store
