#!/usr/bin/env python

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

start = mc.player.getTilePos()

for i in range(1,10):
	mc.setBlock(start.x + i, start.y - 1, start.z -1,  block.GOLD_BLOCK.id)
	mc.setBlock(start.x + i, start.y - 1, start.z,     block.GOLD_BLOCK.id)
	mc.setBlock(start.x + i, start.y - 1, start.z + 1, block.GOLD_BLOCK.id)
