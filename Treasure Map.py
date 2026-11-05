import Utils, Path, Bulk, Move

Utils.initialize()
jump(Unlocks.Treasure_Map)

position = (0, 0)
position_previous = None
while position != position_previous:
    
    ground = get_ground_type()
    while ground != Grounds.Basalt: 
        dig()
        ground = get_ground_type()
    
    position_previous = position
    position = measure()
    Move.to(position)
    
dig()

instructions = measure()

layers = []

destination = (get_pos_x(), get_pos_y())
possible_positions = set()

for character in instructions:
    if destination == None:
        destination = (get_pos_x(), get_pos_y())
        possible_positions.add(destination)
    
    if character == "D":
        layers.append((destination, possible_positions))
        
        possible_positions = set()
        
    else:
        if character == "N":
            destination = (destination[0], destination[1] + 1)
        elif character == "E":
            destination = (destination[0] + 1, destination[1])
        elif character == "S":
            destination = (destination[0], destination[1] - 1)
        elif character == "W":
            destination = (destination[0] - 1, destination[1])
        
        world_size = get_world_size()
        destination = (destination[0] % world_size, destination[1] % world_size)

        possible_positions.add(destination)

for layer in layers:
    start = (get_pos_x(), get_pos_y())
    destination, possible_positions = layer
    path = Path.a_star_clearway(start, destination, possible_positions)
    
    if path == None:
        print("no path found")
        break

    for position in path:
        Move.to(position)
        
    dig()
    
harvest()