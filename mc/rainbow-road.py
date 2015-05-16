#!/usr/bin/env python

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

start = mc.player.getTilePos()

colours= {
	'red' : 14,
	'orange' : 1,
	'yellow' : 4,
	'green' : 5,
	'blue' : 3,
	'indigo' : 11,
	'violet' : 10
}

rainbow = [ 'red', 'yellow', 'orange', 'green', 'blue', 'indigo', 'violet' ]

i = 0
for colour in rainbow:
	mc.setBlock(start.x + i, start.y - 1, start.z - 1, block.WOOL.id, colours[colour])
	mc.setBlock(start.x + i, start.y - 1, start.z,     block.WOOL.id, colours[colour])
	mc.setBlock(start.x + i, start.y - 1, start.z + 1, block.WOOL.id, colours[colour])
	i += 1
	time.sleep(1)
