import Constants, Random

def initialize(size = get_world_size()):
	set_world_size(size)
	clear()
	change_hat(Random.list(Constants.HATS))