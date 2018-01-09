#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import os


class Post(object):

    def __init__(self):
        self.__text = None
        self.__created_at = datetime.datetime.now()

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @text.deleter
    def text(self):
        del (self.__text)

    created_at = property(lambda self: self.__created_at)

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
        print("Was created " + self.filename + " in " + full_path)
        f = open(full_path, 'w')
        for K in strings:
            f.write(K)
            f.write('\n')
            f.write("_________________________________________________________________\n")

    def read_from_console(self):
        pass

    def to_strings(self):
        pass
