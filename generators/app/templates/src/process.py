#!/usr/bin/env python3

import loggz

from loadguard.runners import ProjectStore

LOG = loggz.factory('transilien.louvre_piv.process')
""" The main logger. """


def run(store: ProjectStore):
    """ LoadGuard Task entry point.
    """
    return store
