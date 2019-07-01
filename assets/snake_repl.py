#!/usr/bin/env python3

#Read-Eval-Print Loop for a bash version of snake

#Read in an arrow key press
#If same direction, do nothing
#If opposite direction, do nothing
#If perpendicular to direction of movement, change direction to match arrow

#Print snake to screen, refresh

#Need to parse input: need a way to test input...probably make a 'input' function that only accepts arrow key presses, and as a test puts out a description of the key that was pressed.

#Input
#Read a single key press
#Compare with valid values (Q, Right arrow, Left arrow, Up arrow, Down arrow); if one of the valid arrow key values, output the pressed key.
#If not one of the valid values, output "Key not recognized; press an arrow key or 'Q' to quit.
#If 'Q' was pressed, exit the simulation.

import sys
#print(sys.version_info)
import subprocess
import time

#Test Input and Output to command line
#n = ""
#while(n!='Q'):
#    greeting = "Hello"
#    print(greeting)
#    n = input("Please type your name and press 'Enter': ")
#    if(n=="Q"):
#        print("Goodbye!")
#    else:
#        print(greeting + " " + n + "!")

#Make snake move across the screen
#sky = "\n"
#snake = "---=oooooooooooo<:>="
#trail = " "
#ground = "_"

#for i in range(0,100):
#    subprocess.call("clear")
#    print(20 * sky + i * trail + snake)
#    time.sleep(0.1)

#Demonstrate object moving around screen with arrow keys
#Generate Box
#top = "*"
#side = "|"
#bottom = "*"
#inside = " "

#height = 30

#width = 100
#width_inside = width - 2

#subprocess.call("clear")
#print(width * top + "\n" +
#      height * (side + width_inside * inside + side + "\n") +
#      width * bottom + "\n")

#1. Input
def get_user_input():
    key_press = input()
    return key_press


def test_get_user_input():
    key = get_user_input()
    print(key)


#2. 
def 



def write_display(display: str):
    print(display)


def clear_display():
    subprocess.call("clear")


