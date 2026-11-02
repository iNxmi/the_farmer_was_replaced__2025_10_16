import Utils, Path, Move, Bulk

def parallel():
    
    def execute(position_start):
        y = position_start[1]
        path = Path.horizontal(y)
        
        for position in path:
            Move.to(position)
            dig()
    
    Bulk.horizontal(execute)
    
if __name__ == "__main__":
    Utils.initialize()
    while True:
        parallel()