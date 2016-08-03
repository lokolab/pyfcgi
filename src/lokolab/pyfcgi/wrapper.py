"""
Wrapper for applications in Python via "mod_fcgid".

Copyright (c) Krystian Pietruszka <kpietru@lokolab.net>
License MIT
"""

import os
import sys
from lokolab.pyfcgi.server import PyfcgiServer

class PyfcgiWrapper(object):

    def add_custom_path_to_packages(self, custom_path_to_packages):
        """Adds a custom path to the directory with packages."""
        if isinstance(custom_path_to_packages, str) == False:
            raise TypeError('custom_path_to_packages: invalid type. Must be a str.')

        sys.path.insert(0, custom_path_to_packages)
        return self

    def run(self):
        """Runs the server."""
        # !important Global message for PyfcgiServer()
        os.environ['lokolab.pyfcgi.wrapper'] = 'on'

        server = PyfcgiServer()
        server.run_for_wrapper()

