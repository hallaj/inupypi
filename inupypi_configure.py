#!/usr/bin/env python

from __future__ import with_statement

from optparse import OptionParser
from string import Template
from unipath import Path
import inupypi
import pkgutil

usage = 'usage: %prog [options]'

parser = OptionParser(usage, add_help_option=False)

parser.add_option('--help', action='help',
                  help='show this help message and exit')

parser.add_option('-i', '--virtual-env',
                  default=Path('~/virtualenv/inupypi').expand(),
                  help='Path to Inupypi Virtualenv [default: %default]')

parser.add_option('-k', '--inupypi-home',
                  default=Path(".").cwd(),
                  help='Path to Inupypi Home [default: %default]')

options, args = parser.parse_args()

sample_file = pkgutil.get_data('conf_samples',
                               'httpd-inupypi.conf.sample')


path_of_inupypi = Path(inupypi.__file__).parent.split('site-packages')[0]
site_pkgs = Path(path_of_inupypi, 'site-packages')

mappings = vars(options)
mappings['virtual_env'] = mappings['virtual_env']
mappings['inupypi_home'] = options.inupypi_home
mappings['site_packages'] = site_pkgs
mappings['user'] = raw_input("User for inupypi :") or 'inupypi'
mappings['group'] = raw_input("Group for inupypi :") or 'inupypi'

final_config = raw_input("File to write to: ") or 'inupypi.conf'


template = Template(sample_file)
content = template.safe_substitute(mappings)
with Path(final_config) as final_config:
    final_config.write_file(content)
