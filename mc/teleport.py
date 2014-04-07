The complete program
#!/usr/bin/env python

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
