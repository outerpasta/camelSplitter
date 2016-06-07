#!/usr/bin/python
"""
There is a folder in your home directory called 'camel_splitter'.
Put camelCase files into the 'camel_splitter' directory, then press the button.
The files should be renamed with spaces now.
"""
from Tkinter import *
from os.path import join, dirname, expanduser
from os import listdir, rename, mkdir

CAMEL_DIR = join(expanduser('~'), 'camel_splitter')


def camel_to_spaces(file_name):
    if " " in file_name:
        return file_name
    return ''.join(map(lambda x: x if not x.isupper() else " "+x, file_name))


def do_conversion():
    for f in listdir(CAMEL_DIR):
        rename(
            join(CAMEL_DIR, f),
            join(CAMEL_DIR, camel_to_spaces(f))
        )
    top.destroy()


if __name__ == '__main__':
    try:
        mkdir(CAMEL_DIR)
    except OSError:
        pass

    top = Tk()
    Label(top, text=__doc__).pack()
    Button(top, text='convert!', width=25, command=do_conversion).pack()
    top.mainloop()
