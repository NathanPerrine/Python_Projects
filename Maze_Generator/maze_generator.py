from colorama import init, Fore
import random


#init colorama - needs to be done to use 
init()


def print_maze(maze):
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            cell = maze[i][j]
            if cell == 'u':
                print(Fore.WHITE, f'{cell}', end="")
            elif cell == " ":
                print(Fore.GREEN, f'{cell}', end="")
            else:
                print(Fore.RED, f'{cell}', end="")
        print("\n")


def blank_maze(h, w):
    maze = []
    for i in range(0, h):
        row = []
        for j in range(0, w):
            row.append('u')
        maze.append(row)   
    return maze 


def surrounding_cells(maze, rand_wall):
    s_cells = 0 
    if (maze[rand_wall[0]-1][rand_wall[1]]) == " ":
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]]) == " ":
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1]) == " ":
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]+1]) == " ":
        s_cells += 1

    return s_cells


def main():
    ### Step 1 - Empty Maze
    empty_cell = " "
    maze_wall = "#" 
    start = "O"
    end = "X"
    h = random.randint(5, 15)
    w = random.randint(5, 15)

    maze = blank_maze(h, w)
    # print_maze(maze)

    ### Step 2 - Pick a spot in the maze and set it as a free spot
    ### And then add the walls of it in a list

    # Pick starting point
    starting_height = int(random.random() * h)
    starting_width = int(random.random() * w)

    # Don't start on the edge
    if starting_height == 0:
        starting_height += 1
    if starting_height == h - 1:
        starting_height -= 1

    if starting_width == 0:
        starting_width += 1
    if starting_width == w - 1:
        starting_width -= 1

    # Start the path 
    maze[starting_height][starting_width] = empty_cell
    walls = []
    walls.append([starting_height-1, starting_width])
    walls.append([starting_height+1, starting_width])
    walls.append([starting_height, starting_width-1])
    walls.append([starting_height, starting_width+1])
    
    maze[starting_height-1][starting_width] = maze_wall
    maze[starting_height+1][starting_width] = maze_wall
    maze[starting_height][starting_width-1] = maze_wall
    maze[starting_height][starting_width+1] = maze_wall

    # print_maze(maze)

    ### Step 3 - While there are walls in the list pick a random wall from the list
    # If only one of the two cells that divides the walls is visited 
    # Make the wall a passageand mark the unvisited cell as part of the maze

    while (walls):
        # Pick a random wall 
        rand_wall = walls[int(random.random()*len(walls))-1]
        print(f'{rand_wall=}')
        # Check if left wall
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1]-1] == "u" and maze[rand_wall[0]][rand_wall[1]+1] == " ":
                s_cells = surrounding_cells(maze, rand_wall)
                
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = empty_cell

                    ### Mark new walls 
                    # Upper cell
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0]-1][rand_wall[1]] != empty_cell:
                            maze[rand_wall[0]-1][rand_wall[1]] = maze_wall
                        if [rand_wall[0]-1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Bottom Cell 
                    if rand_wall[0] != h-1:
                        if maze[rand_wall[0]+1][rand_wall[1]] != empty_cell:
                            maze[rand_wall[0]+1][rand_wall[1]] = maze_wall
                        if [rand_wall[0]+1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # Leftmost cell 
                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1]-1] != empty_cell:
                            maze[rand_wall[0]][rand_wall[1]-1] = maze_wall 
                        if [rand_wall[0], rand_wall[1]-1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1]-1])
                
                # Delete wall 
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)
                
                continue

        # Check if an upper wall 
        if rand_wall[0] != 0:
            if maze[rand_wall[0]-1][rand_wall[1]] == "u" and maze[rand_wall[0]+1][rand_wall[1]] == " ":
                s_cells = surrounding_cells(maze, rand_wall)
                
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = empty_cell

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != empty_cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = maze_wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != empty_cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = maze_wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != w-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != empty_cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = maze_wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue
        
        if rand_wall[0] != h-1:
            if maze[rand_wall[0]+1][rand_wall[1]] == "u" and maze[rand_wall[0]-1][rand_wall[1]] == " ":
                s_cells = surrounding_cells(maze, rand_wall)
                
                if (s_cells < 2):
                # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = empty_cell

                    # Mark the new walls
                    if (rand_wall[0] != h-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != empty_cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = maze_wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != empty_cell):
                            maze[rand_wall[0]][rand_wall[1]-1] = maze_wall
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != w-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != empty_cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = maze_wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue
            
        # Check the right wall
        if rand_wall[1] != w-1:
            if maze[rand_wall[0]][rand_wall[1]+1] == "u" and maze[rand_wall[0]][rand_wall[1]-1] == " ":
                s_cells = surrounding_cells(maze, rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = empty_cell

                    # Mark the new walls
                    if (rand_wall[1] != w-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != empty_cell):
                            maze[rand_wall[0]][rand_wall[1]+1] = maze_wall
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != h-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != empty_cell):
                            maze[rand_wall[0]+1][rand_wall[1]] = maze_wall
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (maze[rand_wall[0]-1][rand_wall[1]] != empty_cell):
                            maze[rand_wall[0]-1][rand_wall[1]] = maze_wall
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)
                            break

                continue
        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)
                break

        # Mark remaining unvisited cells as walls
        for i in range(0, h):
            for j in range(0, w):
                if maze[i][j] == 'u':
                    maze[i][j] = maze_wall

        # Entrance and Exit
        for i in range(0, w):
            if maze[1][i] == empty_cell:
                maze[0][i] == start
                break
        for i in range(w-1, 0, -1):
            if maze[h-2][i] == empty_cell:
                maze[h-1][i] = end
                break

    print_maze(maze)

if __name__ == '__main__':
    main()