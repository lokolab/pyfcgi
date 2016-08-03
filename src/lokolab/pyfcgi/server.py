"""
Wrapper for applications in Python via "mod_fcgid".

Copyright (c) Krystian Pietruszka <kpietru@lokolab.net>
License MIT
"""

import os
import sys
import importlib

class PyfcgiServer(object):

    def __init__(self, application=None):
        if application is not None and callable(application) == False:
            raise TypeError('application: invalid type. Must be a class or a function.')

        self.application = application
        self.error_status = '500 Internal Server Error'
        self.error_headers = [('content-type', 'text/plain')]
        self.initialzer = 'pyfcgi_init'

    def run(self):
        if 'lokolab.pyfcgi.wrapper' in os.environ and os.environ['lokolab.pyfcgi.wrapper'] == 'on':
            return self.application
        else:
            self._handle()

    def run_for_wrapper(self):
        self.application = self._process
        self._handle()

    def _handle(self):
        if sys.version_info < (3,0,0):
            namespace = 'flup.server.fcgi'
        else:
            namespace = 'flipflop'

        try:
            handle = importlib.import_module(namespace)
        except ImportError:
            raise ImportError('No module named "' + str(namespace) + '".')

        handle.WSGIServer(self.application).run()

    def _process(self, environ, start_response):
        self._create_os_environ(environ)
        path = environ['SCRIPT_FILENAME']

        if os.access(path, os.R_OK) is False or os.path.getsize(path) == 0:
            start_response(self.error_status, self.error_headers)
            return '[PyfcgiError] The file "' + str(path) + '" is not executable or readable by this process.'

        sys.path.insert(0, os.path.dirname(path))
        filename_ext = os.path.basename(path)
        filename = os.path.splitext(filename_ext)[0]
        handle = __import__(filename)
        try:
            getattr(handle, self.initialzer)
        except AttributeError:
            start_response(self.error_status, self.error_headers)
            return '[AttributeError] Executing failed! The required object "' + str(self.initialzer) + ' = PyfcgiServer(app).run()" does not exist.'
        else:
            return eval('handle.' + str(self.initialzer) + '(environ, start_response)')

    def _create_os_environ(self, environ):
        for key, value in sorted(environ.items()):
            os.environ[str(key)] = str(value)

