import tkinter as tk
from DFS import DFS
from BFS import BFS
from Astar import A_star
from pyamaze import maze as pyamaze_maze, agent, COLOR, textLabel

# Function to run the maze generation and search algorithms
def run_maze():
    # Get the parameters from the GUI inputs
    size_rows = int(size_rows_entry.get())
    size_columns = int(size_columns_entry.get())
    start_x, start_y = map(int, start_position_entry.get().split(','))
    end_x, end_y = map(int, end_position_entry.get().split(','))
    obstacles_percentage = int(obstacles_entry.get())
    selected_method = method_var.get()

    # Close the input window
    input_window.destroy()

    # Create and generate the maze
    maze = pyamaze_maze(size_rows, size_columns)
    maze.CreateMaze(end_x, end_y, loopPercent=obstacles_percentage)

    # Choose the search method based on the selected option
    if selected_method == 'DFS':
        all_search, bfs_path, forward_path = DFS(maze, start=(start_x, start_y))
    elif selected_method == 'BFS':
        all_search, bfs_path, forward_path = BFS(maze, start=(start_x, start_y))
    elif selected_method == 'A_star':
        all_search, bfs_path, forward_path = A_star(maze, start=(start_x, start_y))

    # Create agents and visualize paths
    Agent_1 = agent(maze, start_x, start_y, goal=(end_x, end_y), footprints=True, shape='square', color=COLOR.green)
    Agent_2 = agent(maze, end_x, end_y, goal=(start_x, start_y), footprints=True, filled=True)
    Agent_3 = agent(maze, start_x, start_y, footprints=True, color=COLOR.yellow)

    maze.tracePath({Agent_1: all_search}, showMarked=True)
    maze.tracePath({Agent_2: bfs_path})
    maze.tracePath({Agent_3: forward_path})

    # Display the length of the shortest path and search length
    textLabel(maze, 'Length of shortest Path', len(forward_path) + 1)
    textLabel(maze, 'Length of search', len(all_search))
    maze.run()
   

# Create the input window for collecting parameters
input_window = tk.Tk()
input_window.title("Maze Parameters")

# Create and pack GUI input widgets in the input_window
tk.Label(input_window, text="Maze Size (rows, columns):").pack()
size_rows_entry = tk.Entry(input_window)
size_rows_entry.pack()

size_columns_entry = tk.Entry(input_window)
size_columns_entry.pack()

tk.Label(input_window, text="Start Position (x, y):").pack()
start_position_entry = tk.Entry(input_window)
start_position_entry.pack()

tk.Label(input_window, text="End Position (x, y):").pack()
end_position_entry = tk.Entry(input_window)
end_position_entry.pack()

tk.Label(input_window, text="Obstacles Percentage (1-100):").pack()
obstacles_entry = tk.Entry(input_window)
obstacles_entry.pack()

tk.Label(input_window, text="Select Search Method:").pack()
method_var = tk.StringVar(input_window)
method_var.set('A_star')  # Default method selection
methods = ['DFS', 'BFS', 'A_star']
method_dropdown = tk.OptionMenu(input_window, method_var, *methods)
method_dropdown.pack()

# Create and pack the Start button in the input_window
start_button = tk.Button(input_window, text="Start", command=run_maze)
start_button.pack()

# Run the input window main loop
input_window.mainloop()
