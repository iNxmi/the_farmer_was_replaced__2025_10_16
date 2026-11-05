import Utils, Path, Move, Bulk

def is_valid_position(position):
    return (position[0] + position[1] * 2) % 5 == 0

positions = set()
for position in Path.default():
    if is_valid_position(position):
        positions.add(position)

OFFSETS = {(1, 0), (0, 1), (-1, 0), (0, -1)}
def parallel():

    def execute(position_start):
        y = position_start[1]
        path = Path.horizontal(y)

        path_filtered = []
        for position in path:
            if position in positions:
                path_filtered.append(position)

        counter = {}
        measurements = {}

        for index in range(3):
            for position in path_filtered:
                hover(18)
                Move.to(position)
                    
                for offset in OFFSETS:
                    position_offset = (position[0] + offset[0], position[1] + offset[1])
                    
                    if position_offset[0] < 0:
                        continue
                    if position_offset[0] >= get_world_size():
                        continue
                        
                    if position_offset[1] < 0:
                        continue
                    if position_offset[1] >= get_world_size():
                        continue
        
                    if position_offset not in measurements:
                        hover(0)
                    else:
                        hover(measurements[position_offset])
                    
                    Move.to(position_offset)
                    
                    if get_ground_type() != Grounds.Soil:
                        till()
                        
                    plant(Entities.Bamboo)
                    
                    measurements[position_offset] = measure()
                    
                    Move.to(position)
                    
            for index in range(3):
                do_a_flip()
    
    Bulk.horizontal(execute)
    
if __name__ == "__main__":
    Utils.initialize()
    
    while True:
        parallel()






