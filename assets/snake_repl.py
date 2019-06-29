#!/usr/bin/python3

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

print("Press a key")
