#!/usr/bin/python
# -*- coding: utf-8 -*-

from mPost import Post


class Link(Post):
    def __init__(self):
        Post.__init__(self)
        self.__url = ""

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    def read_from_console(self):
        pass

    def to_strings(self):
        pass
