import Utils, Path, Move

while True:
	Utils.initialize()
	change_hat(Hats.Dinosaur_Hat)
	while True:
		destination = measure()
		if destination == None:
			break
			
		Move.to(destination)