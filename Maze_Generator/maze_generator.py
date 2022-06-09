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
        





def main():
    empty_cell = " "
    wall = "#" 
    start = "O"
    end = "X"
    h = random.randint(5, 15)
    w = random.randint(5, 15)

    maze = blank_maze(h, w)
    print_maze(maze)

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
    walls.append()


if __name__ == '__main__':
    main()