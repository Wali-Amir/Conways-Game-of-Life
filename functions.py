import random
import copy

def random_state(height, width):
    board = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            board[i][j] = random.randint(0,1)
    
    return board

def render(board, height, width):
    print('+',end="-") #top border
    for _ in range(2*width):
        print('-', end='') 
    print('+')

    for row in range(height): #row loop
        print('|',end=" ")
        for col in range(width): #col loop
            if board[row][col] == 1: #if this is head position print X
                print('#',end=' ')
            else:
                print(' ',end=' ')
        print('|') 

    print('+',end="-") #top border
    for _ in range(2*width):
        print('-', end='') 
    print('+')

def next_board_state(board,height,width):
    new_board = copy.deepcopy(board)

    for row in range(height):
        for col in range(width):
            nearby_alive = 0
            state = board[row][col]
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    if (row+i<0 or row+i>=height or col+j<0 or col+j>=width):
                        continue
                    elif (i==0 and j==0):
                        continue
                    elif board[row+i][col+j]==1:
                        nearby_alive+=1
            if state==1 and nearby_alive<2:
                new_board[row][col] = 0
            elif state==1 and nearby_alive<4:
                new_board[row][col] = 1
            elif state==1 and nearby_alive>3:
                new_board[row][col] = 0
            elif state==0 and nearby_alive==3:
                new_board[row][col] = 1
    
    return new_board

def load_board(file_name):
    with open(file_name,'r') as pattern:
        read_board = pattern.read().splitlines()
        our_board = []
        for line in read_board:
            list_line = []
            for i in range(len(line)):
                list_line.append(int(line[i]))
            our_board.append(list_line)
    return our_board