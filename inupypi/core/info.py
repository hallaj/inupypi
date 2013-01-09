#!/usr/bin/env python
# -*- coding: utf8 -*-

from unipath import Path


class Info(object):
    __type__ = None
    __parents__ = None
    __contents__ = None

    def __init__(self, path):
        try:
            path = Path(path)

            self.__parents__ = path
            self.__contents__ = [d.name for d in path.listdir()]
        except:
            pass
