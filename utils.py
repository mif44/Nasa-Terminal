from art import text2art
from tqdm import tqdm


import os
import sys
import time


def terminal_clean():
    os.system("cls")


def terminal_exit():
    sys.exit()


def text_output():
    art_str = text2art("NASA Terminal")
    type_effect(art_str, delay=0.002)


def type_effect(text, delay=0.001) -> str:
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)


def loading_terminal():
    for _ in tqdm(range(100), desc = "Loading", colour="green", ncols = 80):
        time.sleep(0.07)


def launch_terminal():
    terminal_clean()
    loading_terminal()
    terminal_clean()
    text_output()
