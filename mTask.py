#!/usr/bin/python
# -*- coding: utf-8 -*-
from mPost import Post

from datetime import datetime


class Task(Post):
    def __init__(self):
        Post.__init__(self)
        self.__due_date = None

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, value):
        self.__due_date = value


    def read_from_console(self):
        self.text = raw_input("What do you want to do?  ")
        line = raw_input("Date before to do that DD.MM.YYYY for example 12.05.2018  ")
        self.due_date = datetime.strptime(line,"%d.%m.%Y")


    def to_strings(self):
        created_at = "Was created " + datetime.strftime(self.created_at, "%d:%m:%Y %H:%M")
        due_date = "Deadline to " + datetime.strftime(self.due_date, "%d:%m:%Y %H:%M")
        return (created_at, due_date, self.text)