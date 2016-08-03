"""
Wrapper for applications in Python via "mod_fcgid".

Copyright (c) Krystian Pietruszka <kpietru@lokolab.net>
License MIT
"""

import os
import unittest
from lokolab.pyfcgi.wrapper import PyfcgiWrapper

class PyfcgiWrapperTest(unittest.TestCase):

    def test_is_instance(self):
        wrapper = PyfcgiWrapper()
        self.assertIsInstance(wrapper, PyfcgiWrapper)

    def test_add_custom_path_to_packages_with_invalid_argument_custom_path_to_packages_exception(self):
        with self.assertRaises(TypeError):
            wrapper = PyfcgiWrapper()
            custom_path_to_packages = None
            wrapper.add_custom_path_to_packages(custom_path_to_packages)

    def test_add_custom_path_to_packages_returns_self(self):
        wrapper = PyfcgiWrapper()
        custom_path_to_packages = '/somedir'
        ret = wrapper.add_custom_path_to_packages(custom_path_to_packages)
        self.assertIsInstance(ret, PyfcgiWrapper)

    def test_run_checks_global_flag(self):
        wrapper = PyfcgiWrapper()
        wrapper.run()
        self.assertEqual(os.environ['lokolab.pyfcgi.wrapper'], 'on')

if __name__ == '__main__':
    unittest.main()

