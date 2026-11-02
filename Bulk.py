import Thread, Move, Path, Logger

log = Logger.new("Bulk")

def path(path, function):
    threads = list()

    Move.origin()
    length = len(path)
    results = list()
    for index in range(length):
        position = path[index]
        Move.to(position)
        
        def execute():
            return function(position)
        
        if index >= length - 1:
            results.append(execute())
            break
        
        while num_drones() >= max_drones():
            pass
            
        thread = Thread.new(execute)
        threads.append(thread)
        thread["start"]()

    Move.origin()
    while len(threads) > 0:
        thread = threads.pop()
        result = thread["join"]()
        results.append(result)
        
    return results

def horizontal(function):
    positions = Path.vertical(0)
    return path(positions, function)
    
def vertical(function):
    positions = Path.horizontal(0)
    return path(positions, function)
