# Practice_3

# Library
from os import system as sys
from termcolor2 import colored
from pyfiglet import figlet_format

# Clear Terminal
sys('clear')

# Intro
print(colored(figlet_format("Exercises Part 1"), color='cyan'))
print(colored('=====================================================================', color='red'))
print(colored('Question Number ===> 3', color='blue'))
print(colored('// Be Sure To Read The README File To See The Question //', color='blue'))
print('                                            ')

# Value Input
name = input(colored('Enter Name ===> ', color='light_red'))

# Start
print(colored('=====================================================', color='green'))
print(f"Capitalize The First Letter Of The Name ===> {name.capitalize()}")
print(f"Minimize Everything ===> {name.lower()}")
print(f"Capitalize All Letters ===> {name.upper()}")
print(colored('=====================================================', color='green'))


# Finish
# Create By Moein Heshmati