#!/usr/bin/env python

import mcpi.minecraft as minecraft
import mcpi.block as block

# A 'Magic Sword' module.
# This defines a function 'handle_events' that will continually poll
# Minecraft for block hits (right mouse button) with the sword, and
# do some spell on each block hit received.  The spell gets passed
# in to the function.

def handle_events(spell, host="localhost",  mc=None):
	"""
	Does the 'spell' given to it on every block hit.
	The spell is a function such as 'test_spell' below, which
	must have two arguments, one for the minecraft object and one
	for the block 'hit'.
	If you don't pass in 'mc', this will create it, using the 'host'
	parameter, which you can also pass in.
	"""
	if not mc :
		mc = minecraft.Minecraft.create(host)
		mc.postToChat("Magic Sword on")
	try:
		while True:
			hits = mc.events.pollBlockHits()
			if hits:
				for hit in hits:
					spell(mc, hit)
	except KeyboardInterrupt:
		mc.postToChat("Magic Sword off")
		print("Magic Sword off")


def test_spell(mc, hit):
	print("hit: " + str(hit.pos) + str(hit.face))

if __name__ == "__main__":
	handle_events(test_spell)

