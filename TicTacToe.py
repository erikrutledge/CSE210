# Erik Rutledge
# CSE 210
# Tic-Tac-Toe

def display_grid(grid):
    print(f"\n{grid[0]}|{grid[1]}|{grid[2]}\n-+-+-\n{grid[3]}|{grid[4]}|{grid[5]}\n-+-+-\n{grid[6]}|{grid[7]}|{grid[8]}")

def make_selection(i):
    if turn_order[i] == 0:
        selection = int(input("\nX's turn to choose a square: "))
        compare_to_array(selection)
    elif turn_order[i] == 1:
        selection = int(input("\nO's turn to choose a square: "))
        compare_to_array(selection)
    else:
        print("Sorry there was an error defining whose turn it was. Please try again.")

def compare_to_array(selection):
    if turn_order[i] == 0:
        grid[selection-1] = "x"
    elif turn_order[i] == 1:
        grid[selection-1] = "o"
    else:
        print("I'm sorry, I don't know what went wrong")

def check_for_win():
    if grid[0] == grid[1] == grid[2]:
        end_game()
    elif grid[3] == grid[4] == grid[5]:
        end_game()
    elif grid[6] == grid[7] == grid[8]:
        end_game()
    elif grid[0] == grid[3] == grid[6]:
        end_game()
    elif grid[1] == grid[4] == grid[7]:
        end_game()
    elif grid[2] == grid[5] == grid[8]:
        end_game()
    elif grid[0] == grid[4] == grid[8]:
        end_game()
    elif grid[2] == grid[4] == grid[6]:
        end_game()

def check_for_tie(i):
    if i == 8:
        end_game()

def end_game():
    global game_state
    game_state = False
    display_grid(grid)

def main():
        display_grid(grid)
        make_selection(turn_order[i])
        check_for_win()
        check_for_tie(i)




grid = [1,2,3,4,5,6,7,8,9]
turn_order = [0,1,0,1,0,1,0,1,0,1]
i = 0
selection = "starting value"
game_state = True

while game_state == True:
    main()
    i += 1
print("\nGood game!")