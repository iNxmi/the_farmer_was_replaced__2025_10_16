HATS = [
	Hats.Brown_Hat,
	Hats.Cactus_Hat,
	Hats.Carrot_Hat,
	#Hats.Dinosaur_Hat,
	Hats.Gray_Hat,
	Hats.Green_Hat,
	Hats.Purple_Hat,
	Hats.Straw_Hat,
	Hats.Traffic_Cone,
	Hats.Tree_Hat,
	Hats.Sunflower_Hat,
	Hats.Wizard_Hat,
	Hats.Golden_Cactus_Hat,
	Hats.Gold_Hat
]

RIGHT_OF = {
	North: East,
	East: South,
	South: West,
	West: North
}

LEFT_OF = {
	North: West,
	West: South,
	South: East,
	East: North
}

BEHIND_OF = {
	North: South,
	East: West,
	South: North,
	West: East
}

ENTITY_TO_GROUND = {
	Entities.Bush: Grounds.Soil,
	Entities.Cactus: Grounds.Soil,
	Entities.Carrot: Grounds.Soil,
	Entities.Grass: Grounds.Grassland,
	Entities.Pumpkin: Grounds.Soil,
	Entities.Sunflower: Grounds.Soil,
	Entities.Tree: Grounds.Grassland
}