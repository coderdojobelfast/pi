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

