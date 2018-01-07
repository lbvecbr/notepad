#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime, time
import os


class Post(object):
    def __init__(self):
        self.__text = None
        self.__created_at = datetime.datetime.now()

    @property
    def filename(self):
        filename = str(self).split('.')
        filename = filename[0][2:].lower()
        filename += '__' + self.__created_at.strftime("%d-%m-%Y__%H-%M") + '.txt'
        return filename

    def save(self, strings):
        script_dir = os.path.dirname(__file__)
        dirname = "notes"
        full_path = os.path.join(script_dir, dirname, self.filename)
        print(full_path)
        f = open(full_path, 'w')
        for K in strings:
            f.write(K)

    def read_from_console(self):
        pass

    def to_strings(self):
        pass
