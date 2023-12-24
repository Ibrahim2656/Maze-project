from pyamaze import maze,agent,COLOR,textLabel
def DFS(Maze,start=None):
    if start is None:
        start=(Maze.rows,Maze.cols)
    visited=[start]
    frontier=[start]
    dfs_path={}
    all_search=[]
    while frontier:
        curr=frontier.pop()
        all_search.append(curr)
        if curr==Maze._goal:
            break
        poss=0
        for dir in "ESNW":
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
                poss+=1
                visited.append(child)
                frontier.append(child)
                dfs_path[child]=curr
            if poss>1:
                Maze.markCells.append(curr)
    forward_path={}
    cell=Maze._goal
    while cell!=start:
        forward_path[dfs_path[cell]]=cell
        cell=dfs_path[cell]
    return all_search,dfs_path,forward_path
