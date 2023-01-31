from keyboard import add_hotkey
from clipboard import copy
from unidecode import unidecode
from os import popen


def formatarBuffer():
    copy(unidecode(popen("xsel -o").read()).upper())


add_hotkey("ctrl + alt", formatarBuffer)

input("")
