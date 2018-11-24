#!/usr/bin/env python

# Copyright 2014 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# https://github.com/coderdojobelfast/pi.git

# A progam to build (some of) a house.  Uses functions to do the work.

import time
import sys

import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.vec3 import Vec3

# a global variable - these are not normally recommended but
# that's for another tutorial!
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
"""
Replace "raw_input" with "input" for Python 3
width = raw_input("width: ")
depth = raw_input("depth: ")
height = raw_input("height: ")
"""
width = raw_input("width: ")
depth = raw_input("depth: ")
height = raw_input("height: ")
house(corner, int(width), int(depth), int(height))


