#!/usr/bin/env python
# A progam to build (some of) a house.  Uses functions to do the work.

import time
import sys

import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

# a global variable - not normally recommended
mc = minecraft.Minecraft.create()

def plane(c1, c2, material):
	"""Build from one corner to another using the material given"""
	mc.setBlocks(c1.x, c1.y, c1.z, c2.x, c2.y, c2.z, material)

def wall(p1, p2) :
	"""Build a stone wall from p1 to p2"""
	plane(p1, p2, block.STONE.id)
	
def door(p1) :
	"""Place a door (height 2 blocks) at the given position"""
	top = Vec3(0, 1, 0)
	plane(p1, p1 + top, block.DOOR_WOOD.id)

def house(location, east, south, height):
	"""
	Build a house - 'location' becomes the north east corner,
	and the house is 'east' blocks wide toward the east, and
	'south' blocks long toward the south, and 'height' blocks high.
	There is a door in the middle of the north wall.
	"""
	groundNE = location                              # ground north east
	roofSE = groundNE + Vec3(0, height, south)       # roof south east
	roofNW = groundNE + Vec3(east, height, 0)        # roof north west
	groundSW = groundNE + Vec3(east, 0, south)       # ground south west
	wall(groundNE, roofSE)                           # build east wall
	wall(groundNE, roofNW)                           # build north wall
	wall(roofSE, groundSW)                           # build south wall
	wall(roofNW, groundSW)                           # build west wall
	northCentre = Vec3(int(east/2), 0, 0 )           # half way 'east'
	door(groundNE + northCentre)                # add door in north wall


# Build a house just south of the player.
# Uses input function to ask for the dimensions of the house
corner = mc.player.getTilePos() + Vec3(0, 0, 3)
width = raw_input("width: ")
depth = raw_input("depth: ")
height = raw_input("height: ")
house(corner, int(width), int(depth), int(height))


