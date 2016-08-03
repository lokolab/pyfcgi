"""
Wrapper for applications in Python via "mod_fcgid".

Copyright (c) Krystian Pietruszka <kpietru@lokolab.net>
License MIT
"""

import os
import unittest
from lokolab.pyfcgi.server import PyfcgiServer

class PyfcgiServerTest(unittest.TestCase):

    # !important For tests.
    def example_application(self, environ, start_response):
        start_response('200 OK', [('content-type', 'text/html')])
        return '<h1>Hello world!</h1>'

    def test_is_instance(self):
        server = PyfcgiServer()
        self.assertIsInstance(server, PyfcgiServer)

    def test_create_object_with_invalid_argument_application_exception(self):
        with self.assertRaises(TypeError):
            application = 'string'
            PyfcgiServer(application)

    def test_run_returns_object(self):
        os.environ['lokolab.pyfcgi.wrapper'] = 'on'
        application = self
        server = PyfcgiServer(application)
        self.assertIsInstance(server.run(), PyfcgiServerTest)

if __name__ == '__main__':
    unittest.main()

