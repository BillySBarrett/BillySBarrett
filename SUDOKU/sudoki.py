import time
import os
os.system('clear')


def reset_grid():
    grid = []
    for i in range(9):
        horizontal = []
        for i in range(9):
            horizontal.append(0)
        grid.append(horizontal)
    print(grid)

grid = []
index_original = []

# grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
# grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
# grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
# grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
# grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
# grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
# grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
# grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])
# grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])

# grid = [[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]

def read_from_file():
    global grid
    global index_original
    file = open('sudokusave.txt', 'r')
    save = file.readlines()
    grid = eval(save[0])
    index_original = eval(save[1])

def print_grid():
    listgrid = []
    listgrid.append('    0 1 2   3 4 5   6 7 8 ')
    for i in range(3):
      listgrid.append('  +-------+-------+-------+')
      for j in range(3):
         listgrid.append(f'{j+(i*3)} | {grid[j+(i*3)][0]} {grid[j+(i*3)][1]} {grid[j+(i*3)][2]} | {grid[j+(i*3)][3]} {grid[j+(i*3)][4]} {grid[j+(i*3)][5]} | {grid[j+(i*3)][6]} {grid[j+(i*3)][7]} {grid[j+(i*3)][8]} |')
    listgrid.append('  +-------+-------+-------+')
    joingrid = '\n'.join(listgrid)
    os.system('clear')
    print(joingrid)

def get_original():
    global index_original
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                index_original.append((i, j))

def change_values():
    global grid
    x = input('Column (x): ')
    if x == 'done':
        return True

    y = input('Row (x): ')
    if y == 'done':
        return True

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("That's not a number, try again!")
        time.sleep(2)
        return

    if (y, x) in index_original:
        print("That position can't be changed")
        time.sleep(2)
        return

    if x < 0 or x > 9 or y < 0 or y > 9:
        print('Please enter a valid number')
        time.sleep(2)
        return

    change_to = input('Change it to (0-9): ')

    try:
        change_to = int(change_to)
    except ValueError:
        print("That's not a number, try again!")
        time.sleep(2)
        return

    if change_to < 0 or change_to > 9:
        print('Please enter a valid number')
        time.sleep(2)
        return

    grid[y][x] = change_to
    print_grid()

def save_game():
    file = open("sudokusave.txt", 'w')
    file.write(repr(grid) + '\n')
    file.write(repr(index_original))

def checker():
    for i in range(0, 9):

        # FILLED CHECKER
        if 0 in grid[i]:
            return False

        # BOX CHECKER
        for k in range(0, 9, 3):
            boxcheck = []
            for i in range(0, 3):
                for j in range(0, 3):
                    boxcheck.append(grid[j+k][i+((i//3)*3)])
            if len(set(boxcheck)) != 9:
                return False

        # ROW CHECKER
        if len(set(grid[i])) != 9:
            return False

        # COLUMN CHECKER
        columncheck = []
        for j in range(0, 9):
            columncheck.append(grid[j][i])
        if len(set(columncheck)) != 9:
            return False
    return True

def main():
    read_from_file()
    print(grid)
    print(index_original[3])

    print('Welcome to Sudoku!')
    time.sleep(3)
    if index_original == []:
        get_original()
    while True:
        if checker():
            print('Congrats! You solved the puzzle!')
            break
        print_grid()
        x = change_values()
        save_game()
        if x:
            print('Thanks for playing, come again!')
            break
main()
