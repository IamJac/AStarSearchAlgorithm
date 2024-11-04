import heapq
def astar_search(graph,heuristics,start,goal):
    pq=[]
    heapq.heappush(pq,(heuristics[start],start))
    visited=set()
    path_cost={start:0}
    while pq:
        _, current=heapq.heappop(pq)#For proper unpacking of elements from the tuples,the fisrt value is neglected using the _, convention
                                    #We want the node itself,not its heuristic
        if current==goal:
            print(current,end=",")
            return
        if current not in visited:
            print(current,end=",")
            visited.add(current)
            for neighbors,cost in graph.get(current,[]):
                tentative_path_cost=path_cost[current] + cost
                if neighbors not in visited and tentative_path_cost<path_cost.get(neighbors,float('inf')):
                    path_cost[neighbors]=tentative_path_cost
                    total_path_cost=tentative_path_cost + heuristics[neighbors]
                    heapq.heappush(pq,(total_path_cost,neighbors))

def manhattan_distances(goal,position):
    gx,gy=goal
    px,py=position
    return abs(gx-px) + abs(gy-py)

Grid={'A':(0,0),'B':(1,0),'C':(2,0),'D':(3,0),'E':(3,1),'F':(2,1),'G':(1,1),'H':(0,1),
      'I':(0,2),'J':(1,2),'K':(2,2),'L':(3,2)}
Graph={'A':[('B',1),('H',1)],'B':[('A',1),('C',1),('G',1)],'C':[('B',1),('D',1),('F',1)],
       'D':[('E',1),('C',1)],'E':[('D',1),('F',1),('L',1)],
       'F':[('E',1),('C',1),('G',1),('K',1)],'G':[('B',1),('H',1),('J',1),('F',1)],
       'H':[('A',1),('G',1),('I',1)],'I':[('H',1),('J',1)],'J':[('I',1),('G',1),('K',1)],
       'K':[('J',1),('F',1),('L',1)],'L':[('K',1),('E',1)]}
print("Enter the goal position below(Uppercase-from A-L)")
goal_position=input("Goal position = ")
Heuristics={'A':manhattan_distances(Grid[goal_position],Grid['A']),'B':manhattan_distances(Grid[goal_position],Grid['B']),
            'C':manhattan_distances(Grid[goal_position],Grid['C']),'D':manhattan_distances(Grid[goal_position],Grid['D']),
            'E':manhattan_distances(Grid[goal_position],Grid['E']),'F':manhattan_distances(Grid[goal_position],Grid['F']),
            'G':manhattan_distances(Grid[goal_position],Grid['G']),'H':manhattan_distances(Grid[goal_position],Grid['H']),
            'I':manhattan_distances(Grid[goal_position],Grid['I']),'J':manhattan_distances(Grid[goal_position],Grid['J']),
            'K':manhattan_distances(Grid[goal_position],Grid['K']),'L':manhattan_distances(Grid[goal_position],Grid['L'])}
print("Enter the starting point below(Uppercase-from A-L)")
start_position=input("Start position = ")
astar_search(Graph,Heuristics,start_position,goal_position)
