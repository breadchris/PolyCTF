import SocketServer, sys, random, struct
from threading import Thread

MAZE_WIDTH  = 20
MAZE_HEIGHT = 20

BOTTOMWALL = 0
RIGHTWALL  = 1
VISITED    = 2

NORTH = 0
SOUTH = 1
WEST  = 2
EAST  = 3


class Maze:
    def __init__( self, n_rows, n_cols ):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.maze = [None]*n_rows

        for i in range(n_rows):
            self.maze[i] = [None]*n_cols
            for j in range(n_cols):
                self.maze[i][j] = [True,True,False] # BOTTOMWALL,RIGHTWALL,VISITED

        currCol = random.randrange(n_cols)
        currRow = random.randrange(n_rows)

        if n_rows*n_cols > sys.getrecursionlimit():
            sys.setrecursionlimit( n_rows*n_cols+5 )

        self._make_path( currRow, currCol )


    def _make_path( self, R, C, D=None ):
        maze = self.maze # speed up a bit

        maze[R][C][VISITED] = True;

        if   D==NORTH: maze[R]  [C]  [BOTTOMWALL] = False
        elif D==SOUTH: maze[R-1][C]  [BOTTOMWALL] = False
        elif D==WEST:  maze[R]  [C]  [RIGHTWALL]  = False
        elif D==EAST:  maze[R]  [C-1][RIGHTWALL]  = False

        directions = []
        if R>0            : directions.append(NORTH)
        if R<self.n_rows-1: directions.append(SOUTH)
        if C>0            : directions.append(WEST)
        if C<self.n_cols-1: directions.append(EAST)

        dir_len = len(directions)
        for i in range(dir_len):
            j = random.randrange(dir_len)
            directions[i],directions[j] = directions[j],directions[i]

        for dir in directions:
            if dir==NORTH:
                if not maze[R-1][C][VISITED]:
                    self._make_path( R-1,C,NORTH )
            elif dir==SOUTH:
                if not maze[R+1][C][VISITED]:
                    self._make_path( R+1,C,SOUTH )
            elif dir==EAST:
                if not maze[R][C+1][VISITED]:
                    self._make_path( R,C+1,EAST )
            elif dir==WEST:
                if not maze[R][C-1][VISITED]:
                    self._make_path( R,C-1,WEST )


    def print_maze(self, pos):
        result = '.' + self.n_cols*'_.'
        result += '\n'

        for i in range(self.n_rows):
            result += '|'

            for j in range(self.n_cols):
                if i == pos[0] and j == pos[1]:
                    result += "X"
                else:
                    if i==self.n_rows-1 or self.maze[i][j][BOTTOMWALL]:
                        result += '_'
                    else:
                        result += ' '
                if j==self.n_cols-1 or self.maze[i][j][RIGHTWALL]:
                    result += '|'
                else:
                    result += '.'

            result += '\n'

        return result

class Oracle:

    def __init__(self):
        self.maze = Maze(MAZE_WIDTH, MAZE_HEIGHT)
        self.position = [0, 0]
        self.move = ""

    def response(self):
        move = self.move
        r, c = self.position
        maze = self.maze
        maze_grid = self.maze.maze
        if move == "h":
            if c == 0 or maze_grid[r][c-1][RIGHTWALL]:
                return False
            else:
                return True
        elif move == "j":
            if r == maze.n_rows or maze_grid[r][c][BOTTOMWALL]:
                return False
            else:
                return True
        elif move == "k":
            if r == 0 or maze_grid[r-1][c][BOTTOMWALL]:
                return False
            else:
                return True
        elif move == "l":
            if c == maze.n_cols or maze_grid[r][c][RIGHTWALL]:
                return False
            else:
                return True

    def commit(self):
        move = self.move
        if move == "h":
            self.position[1] += -1
        elif move == "j":
            self.position[0] += 1
        elif move == "k":
            self.position[0] += -1
        elif move == "l":
            self.position[1] += 1

        if self.position[0] == MAZE_WIDTH and \
            self.position[1] == MAZE_HEIGHT:
            return True
        else:
            return False

    def print_maze(self):
        print self.maze.print_maze(self.position)

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 9010
    FLAG = 'flag{YOU_ARe_SO_A-MAZE-ING_:D}'

    class SingleTCPHandler(SocketServer.BaseRequestHandler):
        def handle(self):
            try:
                o = Oracle()
                self.request.send("You have been blind folded and are told to solve a maze that you have been placed in. You can move with h, j, k and l.")
                while True:
                    o.print_maze()
                    self.request.send("\nmove: ")
                    move = self.request.recv(2)[0]
                    o.move = move
                    if o.response():
                        self.request.send("[+] You can move in that direction, do you want to go there? (y/n): ")
                        confirm = self.request.recv(2)[0]
                        if confirm == "y":
                            if o.commit():
                                self.request.send("You solved the maze! " + FLAG)
                    else:
                        self.request.send("[-] You cannot move in that direction")
            except:
                self.request.close()

    class DangerousTakeThisServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
        daemon_threads = True
        allow_reuse_address = True

        def __init__(self, server_address, RequestHandlerClass):
            SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)

    if __name__ == "__main__":
        server = DangerousTakeThisServer((HOST, PORT), SingleTCPHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            sys.exit(0)

