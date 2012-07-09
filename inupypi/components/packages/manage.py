#!/usr/bin/env python
# -*- coding: utf8 -*-

import pkgtools.pkg
import tempfile

from inupypi import abort, app
from inupypi.components.packages import get_package_path
from unipath import Path
from werkzeug import secure_filename

def upload_package(uploaded_file):
    filename = secure_filename(uploaded_file.filename)
    workspace = Path(tempfile.mkdtemp())
    temp_save = Path(workspace, filename)

    uploaded_file.save(temp_save)
    package = pkgtools.pkg.SDist(temp_save)
    package_dir = Path(get_package_path(), package.name)
    package_dir.mkdir()
    temp_save.move(Path(package_dir, filename))

    workspace.rmtree()
