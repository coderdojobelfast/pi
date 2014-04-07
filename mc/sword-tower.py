#!/usr/bin/env python
import mcpi.block as block

# import our module!
from sword import handle_events

# Uses the 'sword' module, and builds a small tower of blocks
# on each sword hit, a couple of paces to the east of the player.

def build_tower(mc, pos, block) :
	mc.setBlock(pos.x+2, pos.y, pos.z, block)
	mc.setBlock(pos.x+2, pos.y+1, pos.z, block)
	mc.setBlock(pos.x+2, pos.y+2, pos.z, block)

def build_tower_beside_me(mc, hit):
	print("hit at: " + str(hit.pos) + ", face: " + str(hit.face))
	mc.postToChat("Shazam!")
	pos = mc.player.getPos()
	build_tower(mc, pos, block.STONE)

handle_events(build_tower_beside_me)

