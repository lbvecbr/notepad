#!/usr/bin/python
# -*- coding: utf-8 -*-


from os import mkdir

from mLink import Link
from mMemo import Memo
from mTask import Task

try:
    mkdir('notes')
except WindowsError:
    pass

types = {1: Memo(), 2: Link(), 3: Task()}


def create(type_index):
    if type_index > 0 and type_index <= 3:
        return types[type_index]
    else:
        return None


def main():
    while True:
        try:
            idx = input("Какую запись Вы хотите создать? "
                        "\n 1.Памятка \n 2.Ссылка \n 3.Задача \n ")
        except NameError:
            continue
        post = create(idx)
        if post is not None:
            break

    post.read_from_console()
    post.save(post.to_strings())


if __name__ == "__main__":
    main()
