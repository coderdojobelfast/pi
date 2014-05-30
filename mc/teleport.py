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

# A teleport program.  Starting the program activates the teleporter
# with a destination where you are standing.  To build a teleport pad
# make a block of glass and walk on top of it.  This will teleport you
# back to where you started!

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

start = mc.player.getTilePos()
co_ords = str(start.x) + ", " + str(start.y) + ", " + str(start.z)
mc.postToChat("Teleport activated at " + co_ords)

while True: 
	time.sleep(0.3)
	p = mc.player.getTilePos()
	block_below = mc.getBlock(p.x, p.y - 1, p.z)
	
	if block_below == block.GLASS.id :
		# teleport!
		print("Teleporting")
		mc.setBlock(p.x, p.y, p.z, block.GLOWING_OBSIDIAN)
		mc.setBlock(p.x, p.y+1, p.z, block.GLOWING_OBSIDIAN)
		time.sleep(1)              # give us time to see it!
		mc.player.setPos(start.x, start.y, start.z)   # jump
		# now clear the teleport again
		mc.setBlock(p.x, p.y, p.z, block.AIR)
		mc.setBlock(p.x, p.y+1, p.z, block.AIR)
