from pyamaze import maze,agent,COLOR,textLabel
from collections import deque
def BFS(Maze,start=None):
    if start is None:
        start=(Maze.rows,Maze.cols)
    visited=[start]
    frontier=deque()
    frontier.append(start)
    bfs_path={}
    all_search=[]
    while frontier:
        curr=frontier.popleft()
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
                if child in visited:
                    continue
                frontier.append(child)
                visited.append(child)
                bfs_path[child]=curr
                all_search.append(child)
    forward_path={}
    cell=Maze._goal
    while cell!= start:
        forward_path[bfs_path[cell]]=cell
        cell=bfs_path[cell]
    return all_search,bfs_path,forward_path
