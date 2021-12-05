#! /usr/bin/env python3


fdata = open("report.txt", 'r')

bingo_hits = [int(hit) for hit in fdata.readline().rstrip().split(',')]

bingo_games = []
game = []
# Init array of bingo games from file
for emptyl in fdata:
    for line in range(0, 5):
        game.append([[int(i), '-'] for i in next(fdata).rstrip().split()])
    bingo_games.append(game)
    game = []

winned_games = ['-' for i in range(0, len(bingo_games))]

print("pocet her: ", len(bingo_games))
# print("hits: ", bingo_hits)

def mark_number(game, number):
    for ir, row in enumerate(game):
        for ic, col in enumerate(row):
            if col[0] == number: #and col[1] == '-':
                col[1] = 'x'
                return (ir, ic)
    # print("number", number, "cant be found in this board")
    return None

def check_win(game, last_number):
    """
    Check only line and col with newly marked number.
    if it is in the middle of board, check diagonals aswell.
    """

    # Check row
    x_count = 0
    for y in game[last_number[0]]:
        # print("y", y)
        if y[1] == 'x':
            x_count += 1
            if x_count == 5:
                return True

    # Check column
    x_count = 0
    for x in range(0, 5):
        xnum = game[x][last_number[1]]
        # print("x", xnum)
        if xnum[1] == 'x':
            x_count += 1
            if x_count == 5:
                return True

    # Note: No diagonals for this task   
    # Check diagonals
    # x_count = 0
    # if last_number[0] == last_number[1]:
    #     for i in range(0, 5):
    #         if game[i][i][1] == 'x':
    #             x_count += 1
    #             if x_count == 5:
    #                 return True

    # Check diagonals
    # x_count = 0
    # if (last_number[0] + last_number[1]) == 4:
    #     for i in range(0, 5):
    #         if game[i][4-i][1] == 'x':
    #             x_count += 1
    #             if x_count == 5:
    #                 return True

    return False


def print_board(game):
    print("board:")
    for line in game:
        print(line)

def count_unmarked(game):
    summary = 0
    for line in game:
        for num in line:
            if num[1] == '-':
                summary += num[0]
    return summary


## proceed here
### prozkoumat pouze ty lines, kde byl hit.
win = False
win_game = None
win_game_cnt = 0
win_num = None
for number in bingo_hits:
    # mark this number in all games
    for n, game in enumerate(bingo_games):
        if winned_games[n] == 'x':
            continue
        # print("Marking hit number", number, "in game ", n)
        marked = mark_number(game, number)
        # if number == 13:
            # print_board(game)
        if marked is None:
            print("marked is None", marked, "continue")
            continue
        win = check_win(game, marked)
        if win == True:
            print("BINGO - board", n)
            win_game = game
            win_game_cnt += 1
            win_num = number
            winned_games[n] = 'x'
            print_board(game)
            # if win_game_cnt == len(bingo_games) - 1:
                # break   
            # break
    # if win == True:
        # break

summ = count_unmarked(win_game)
print("Win summary", summ)
print("Final summary", summ * win_num)

fdata.close()
