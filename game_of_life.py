import functions
import time

# Random Starting Grids (Soups)

board_height = 10
board_width = 10
our_board = functions.random_state(board_height,board_width)
functions.render(our_board,board_height,board_width)
while True:
    time.sleep(0.5)
    our_board = functions.next_board_state(our_board,board_height,board_width)
    functions.render(our_board,board_height,board_width)

#Text File

# read_board = functions.load_board("blinker.txt")
# board_height = len(read_board)
# board_width = len(read_board[0])
# functions.render(read_board,board_height,board_width)
# while True:
#     time.sleep(0.5)
#     read_board = functions.next_board_state(read_board,board_height,board_width)
#     functions.render(read_board,board_height,board_width)