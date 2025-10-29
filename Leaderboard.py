def sim(filename, speedup):
	unlocks = {}
	items = {}
	globals = {}
	seed = -1
	simulate(filename, unlocks, items, globals, seed, speedup)
	
if __name__ == "__main__":
	sim("LeaderboardFR2", 100)