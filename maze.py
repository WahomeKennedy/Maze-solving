def print_maze(maze):
    for line in maze:
        print('   ', end='')
        for cell in line:
            if cell == 1:
                print(colored('##', 'red'), end='')
            elif cell == 0:
                print('  ', end='')
            else:
                print(colored('**', 'green'), end='')
        print('\n', end='')

def solve_maze(maze, startX, startY, endX, endY):
    visited = []
    for x, line in enumerate(maze):
        visited.append([])
        for cell in line:
            visited[x].append(cell)
    
    visited[startX][startY] = 2
    currX = startX
    currY = startY
    
    options = []

    while currX != endX or currY != endY:
        if currX+1 < len(maze[currX]) and maze[currX+1][currY] == 0 and visited[currX+1][currY] !=2:
            options.append(Point(currX+1, currY))

        if currX-1 >= 0 and maze[currX-1][currY] == 0 and visited[currX-1][currY] !=2:
            options.append(Point(currX-1, currY))
        
        if currY+1 < len(maze[currX]) and maze[currX][currY+1] == 0 and visited[currX][currY+1] !=2:
            options.append(Point(currX, currY+1))
        
        if currY-1 >= 0 and maze[currX][currY-1] == 0 and visited[currX][currY-1] !=2:
            options.append(Point(currX, currY-1))

        if len(options) == 0: # no options means nowhere to go
            return None
        
        go_to_point = options.pop()
        currX = go_to_point.x
        currY = go_to_point.y
        visited[currX][currY] = 2

        return visited

    """class Point:
        def __init__(self, x,y):
            self.x = x
            self.y = y"""


