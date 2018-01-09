#!/usr/bin/python
# -*- coding: utf-8 -*-

from mPost import Post

from datetime import datetime

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
        self.url = raw_input("Url of the link:  ")
        self.text = raw_input("What is the link?:  ")

    def to_strings(self):
        created_at = "Was created " + datetime.strftime(self.created_at, "%d:%m:%Y %H:%M")
        return (created_at, self.url, self.text)