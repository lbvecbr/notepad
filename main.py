#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import mkdir
from mPost import Post
from mLink import Link
from mMemo import Memo
from mTask import Task

try:
    mkdir('notes')
except WindowsError: pass

post = Post()
link = Link()
memo = Memo()
task = Task()
post.save(["dimon hello", " and bay-bay"])
link.save(["это мой линк"])
memo.save(["это моя мема"])
task.save(["это моё задание"])
