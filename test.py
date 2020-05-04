import random
players = [[0, 4500, 10, 6, 4],
           [1, 4500, 5, 2 ,3],
           [2, 4500, 3, 1, 2],
           [3, 4500, 12, 6, 6]]

# print(random.choice(players))
for i in range(10):
    winning = random.randint(0, 10000)
    # print(winning)


winPlayer1 = [0, 5000]
winPlayer2 = [5001, 10000]
com = 200
winPlayer1[1] += com
winPlayer2[0] += com
# print(winPlayer1,winPlayer2)

def game_play(player1: list, player2: list):
    winPlayer1 = [0, 5000]
    winPlayer2 = [5001, 10000]

    compensation = player1[1] - player2[1]

    winPlayer1[1] += compensation
    winPlayer2[0] += compensation

    win = random.randint(0, 10000)

    if win <= winPlayer1[1]:
        return 1
    else:
        return 2

player1 = [1, 5500, 5, 2 ,3]
player2 = [2, 5000, 5, 2, 3]
for i in range(10):
    print(game_play(player1, player2))