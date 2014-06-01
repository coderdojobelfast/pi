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

# This is sort of "Project 1" + "Project 3".  We're going to use the
# Magic Sword (Project 3) to set the teleport destination (Project 1).
# Trouble is, the 'handle_events' from Magic Sword is an infinite loop,
# and so is the "while True" below. How can a program run two loops
# at once?  Answer: use a thread. A thread is a way of running some
# code at the same time as the rest of your program.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from sword import handle_events
from threading import Thread

# Let's make a "magic spell" function that sets the teleport start pos.
def set_start(mc,hit):
	global startPos 
	startPos = hit.pos
	co_ords = str(start.x) + ", " + str(start.y) + ", " + str(start.z)
	mc.postToChat("Teleport activated at " + co_ords)

# We'll use a thread to run the handle_events function (which contains
# a loop that doesn't finish, so needs its own thread to run in).
class SwordThread(Thread):
	# the __init__() method is used to set the thread up, ready to run.
	def __init__(self):
		Thread.__init__(self)
	# the 'run' method contains the stuff the thread actually does.
	def run(self):
		handle_events(set_start)

# OK let's start the program. Our start position is a global variable.
# One of these days we're going to have to learn how to do without these
# but one thing at a time.
startPos = None

# To use our thread we have to first create it, by the call below...
sword_thread = SwordThread()
# ... and to get it going we have to call its 'start' function.
sword_thread.start()

# The rest is just the same as in Project 1.
mc = minecraft.Minecraft.create()
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
