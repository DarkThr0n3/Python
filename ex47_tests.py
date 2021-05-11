from nose.tools import *
from game import Room
from choot import chootiya

#import ex47
def test_room():
	gold = Room("Goldroom",
				"""This room has gold in it you can grab. Theres a door to the north""")
	assert_equal(gold.name,"Goldroom")
	assert_equal(gold.paths, {})

def test_room_paths():
	centre = Room("Centre","Test room in the centre.")
	north = Room("North", "Test room in the north")
	south = Room("South","Test room in the south")

	centre.add_paths({'north':north, 'south' :south})
	assert_equal(centre.go('north'), north)
	assert_equal(centre.go('south'),south)

def test_map():
	start = Room("Start","You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dngeon","It's dark down here, you can go up")
	start.add_paths({'west':west,'down':down})
	west.add_paths({'east':start})
	down.add_paths({'up':start})

	assert_equal(start.go('west'),west)
	assert_equal(start.go('west').go('east'),start)
	assert_equal(start.go('down').go('up'), start)



