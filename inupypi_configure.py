#!/usr/bin/env python

from __future__ import with_statement

from optparse import OptionParser
from string import Template
from distutils.sysconfig import get_python_lib
from unipath import Path

usage = 'usage: %prog [options]'

parser = OptionParser(usage, add_help_option=False)

parser.add_option('--help', action='help',
                  help='show this help message and exit')

parser.add_option('-i', '--virtual-env',
                  default=Path('~/virtualenv/inupypi').expand(),
                  help='Path to Inupypi Virtualenv [default: %default]')

parser.add_option('-k', '--inupypi-home',
                  default=Path('~/inupypi').expand(),
                  help='Path to Inupypi Home [default: %default]')

options, args = parser.parse_args()

config_file = 'httpd-inupypi.conf'
sample_file = config_file + '.sample'

mappings = vars(options)
mappings['virtual_env'] = mappings['virtual_env']
mappings['inupypi_home'] = mappings['inupypi_home']
mappings['site_packages'] = get_python_lib()
mappings['user'] = raw_input("User for inupypi :") or 'inupypi'
mappings['group'] = raw_input("Group for inupypi :") or 'inupypi'

print 'Creating config file %s with mappings %s' % (config_file,
                                                    mappings)

with open(sample_file) as f1:
    template = Template(f1.read())
    content = template.safe_substitute(mappings)
    with open(config_file, 'w') as f2:
        f2.write(content)
