

def initialize_simulation(board):
    global robot_pos
    global robot_dir

    walls = [tuple(x) for x in board['walls']]
    start = (10,10)
    robot_pos = start
    robot_dir = (1,0)

    def add_v(x,y):
        return(x[0]+y[0],x[1]+y[1])

    # for the testing part
    def Move():
        """ Returns True if moves, False it hits wall"""
        global robot_pos
        
        #next possible position of robot after moving
        next_temp = add_v(robot_pos, robot_dir)
        if next_temp not in walls:
            robot_pos = next_temp
            print (robot_pos)
            
            return True
        else :
            return False

    def RotateRight():
        global robot_dir
        print ("rotate")
        if robot_dir == (1,0):
            robot_dir = (0,-1)
        elif robot_dir == (0,-1):
            robot_dir = (-1,0)
        elif robot_dir == (-1,0):
            robot_dir = (0,1)
        else: robot_dir = (1,0)

    return Move, RotateRight


def irobot_clean(Move, RotateRight):
    # defining the edges for the irobot
    start_pos=(0,0)
    current_pos=start_pos
    direction = (1,0) 
    
    def add_v(x,y):
        return(x[0]+y[0],x[1]+y[1])
    
   # is there a path between a,b 
    Edges={} 
    
    visited={start_pos}
    
    while True:
        path = get_closest_unexplored(visited, Edges, current_pos)
        if path is None: break
            
        next_pos = add_v(current_pos, direction)
        if next_pos == path[0]:
        
            status = Move()
            Edges[(current_pos, next_pos)] = status

            # updating position - no wall   
            if status: 
                current_pos = next_pos
                visited.add(current_pos)
                continue
                
        # updating the direction - point towards path[0]
        RotateRight()
        if direction ==(1,0):
            direction = (0,-1)
        elif direction == (0,-1):
            direction = (-1,0)
        elif direction==(-1,0):
            direction =(0,1)
        else : direction = (1,0)     


# BFS (https://en.wikipedia.org/wiki/Breadth-first_search)
def get_unexplored_distances(visited, edges, root):
    q =[]    # list of vertices to work on currently  
    d = {}   # distances from root, current position
    prev={}  # each vertex and its predecessor
    scanned = set()    
    
    d[root] = 0
    q.append(root)
    
    while q:
        v = q[0]   # what we are currently processing vertex
        del q[0]
        if v in visited: # group of vertices we want to scan
            (x, y) = v
            l = [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]  # adjacent
            for p in l:
                if ((v, p) not in edges or edges[(v, p)] == True)  \
                         and p not in scanned :  # only scan neighbor if there is no red edge (or we don't know), and it was not scanned before in the current computation
                    scanned.add(p)
                    q.append(p)   # adds at the end
                    d[p] = d[v] + 1
                    prev[p] = v   # key is the vertex, value is its predecessor
    return (d,prev)


def get_closest_unexplored(visited, edges, root):
    (d,prev) = get_unexplored_distances(visited, edges, root)
    dom = set(d.keys()) - visited
    if dom:        
        goal = min(dom,key= lambda x: d[x])
        cur = goal
        path = []
        while cur is not root:
            path.insert(0, cur)
            cur = prev[cur]
        return path
    else:
        return None  # no reachable unexplored nodes


# TODO this has to be in server.py
if 0:
    import json

    J = '{"walls":[[13,7],[11,7],[12,7],[11,6],[11,5],[11,4],[11,3],[11,2],[10,2],[9,2],[8,2],[7,2],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7],[7,7],[7,8],[7,9],[6,9],[6,10],[6,11],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[13,12],[13,11],[13,10],[13,9],[13,8]]}'
    board = json.loads(J)

    Move, RotateRight = initialize_simulation(board)
    irobot_clean(Move, RotateRight)
