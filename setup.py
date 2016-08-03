import sys
import re
from setuptools import setup, find_packages

required = []
if sys.version_info < (3,0,0):
    required.append('flup == 1.0.2')
else:
    required.append('flipflop == 1.0')
    #required.append('flipflop >= 1, < 2')

setup(
    name = 'lokolab.pyfcgi',
    version = re.findall('- Version:\s*([^\s]+)', open('README.md').read())[0],

    package_dir = {'':'src'},
    packages = find_packages('src'),
    # !important See lokolab/__init__.py
    namespace_packages = ['lokolab'],

    install_requires = required,
    author = 'Krystian Pietruszka',
    author_email = 'kpietru@lokolab.net',
    description = 'Wrapper for applications in Python via "mod_fcgid".',
    long_description = open('README.md').read(),
    keywords = 'fcgi fastcgi server mod_fcgid wrapper apache wsgi',
    url = 'http://www.lokolab.net',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

