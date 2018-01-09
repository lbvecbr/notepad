#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from mPost import Post


class Memo(Post):
    def __init__(self):
        Post.__init__(self)
        self.text = ""

    def read_from_console(self):
        print("New memo(all of that before string \"end\")")
        while (True):
            line = raw_input()
            if (line == "end"): break
            self.text += line + '\n'

    def to_strings(self):
        created_at = "Was created " + datetime.strftime(self.created_at, "%d:%m:%Y %H:%M")
        return (created_at, self.text)
