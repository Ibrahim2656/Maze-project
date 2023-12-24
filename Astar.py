from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)
def A_star(Maze,start=None):
    if start is None:
        start=(Maze.rows,Maze.cols)
    g_score={cell:float('inf') for cell in Maze.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in Maze.grid}
    f_score[start]=h(start,Maze._goal)
    pq=PriorityQueue()
    pq.put((h(start,Maze._goal),h(start,Maze._goal),start))
    astar_path={}
    all_search=[start]
    while not pq.empty() :
        curr=pq.get()[2]
        all_search.append(curr)
        if curr==Maze._goal:
            break
        for dir in 'ESNW':
            if Maze.maze_map[curr][dir]==True:
                if dir=='E':
                    child=(curr[0],curr[1]+1)
                elif dir=='W':
                    child=(curr[0],curr[1]-1)
                elif dir=='N':
                    child=(curr[0]-1,curr[1])
                elif dir=='S':
                    child=(curr[0]+1,curr[1])
                new_gscore=g_score[curr]+1
                new_fscore=new_gscore+h(child,Maze._goal)
                if new_fscore < f_score[child]:
                    g_score[child]=new_gscore
                    f_score[child]=new_fscore
                    pq.put((new_fscore,h(child,Maze._goal),child))
                    astar_path[child]=curr
    forward_path={}
    cell=Maze._goal
    while cell !=start:
        forward_path[astar_path[cell]]=cell
        cell=astar_path[cell]
    return all_search,astar_path,forward_path









