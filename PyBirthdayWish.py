#!/usr/bin/python3

import os, random
from threading import Thread
from time import sleep
import vlc
from rich.console import Console
from rich.text import Text
from config import *

# Setup rich console
console = Console()

# Importing module specified in the config file
art = __import__(f'arts.{artFile}', globals(), locals(), ['*'])

def replaceMultiple(mainString, toBeReplace, newString):
    for elem in toBeReplace:
        if elem in mainString:
            mainString = mainString.replace(elem, newString)
    return mainString

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def pprint(art, time):
    color_used = [random.choice(color)]
    colorAttribute = []
    for i in range(len(art)):
        line = art[i]
        if line in colorCodes:
            symbol = line
            if symbol == '⑨':
                colorAttribute = ['blink']
            elif symbol == '⑩':
                colorAttribute = []
            elif symbol == '®':
                color_used = color
            else:
                color_used = [colorCodes[symbol]]

        clean_line = replaceMultiple(line, colorCodes, '')
        chosen_color = random.choice(color_used)
        style = chosen_color
        if 'blink' in colorAttribute:
            style += ' blink'

        console.print(Text(clean_line, style=style), end='')
        sleep(time)

def pAudio():
    if playAudio:
        p = vlc.MediaPlayer(resource_path(audio))
        p.play()

with open(resource_path(__file__)) as f_in:
    code = f_in.read()

def pcode():
    if codePrint:
        for i in range(len(code)):
            console.print(Text(code[i], style=codeColor), end='')
            sleep(codingSpeed)
        input('\n\n')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        input('press F11 and hit {Enter}...')
        os.system('cls' if os.name == 'nt' else 'clear')

os.system('cls' if os.name == 'nt' else 'clear')

try:
    pcode()
    Thread(target=pAudio).start()
    Thread(target=pprint, args=(art.mainArt, speed)).start()
    input()

except KeyboardInterrupt:
    console.print('\n[-] Thanks!!', style='red')
    os._exit(0)