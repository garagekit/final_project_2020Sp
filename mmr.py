import random
import math
import matplotlib.pyplot as plt


initialMMR = 2000
# the initialMMR value of each player
changeMMR = 40
# The changeMMR value is the change of each player's MMR value after each match,
# which means that if a player win/lose a match, then his MMR point would
# increase/decrease 40 points.
battleMMRgap = 1000
#the maximum MMR difference between two players in a randomly matched game


def generate_players(number: int):
    '''
    This function was implemented for generating the list of the basic
    information of players, including the playerID, the MMRs, the total number
    of match played, the total number of Ws and the total number of Ls.
    :param number: the total number of players in this experiment
    :return: the list of the basic info of players
    '''
    players = [[0]*5 for _ in range(number)]
    for i in range(number):
        players[i][0] = i
        # players[i][1] = initialMMR
    return players

def assign_players_match(players: list):
    '''
    This function was implemented for assigning players to battle in a single
    round. There are two conditions that would make the assigned match not
    proceed.
    1. If the playerID of the assigned opponent was the same as the matching
    player, the battle would not proceed.
    2. If the MMRs of the two players differ more than the maximum MMR gap, the
    battle would not proceed.
    :param players: the list of the basic information of players
    :return  players: the updated list of the basic information of players after
    a round of matches
    '''
    for i in range(len(players)):
        player1 = players[i]
        assignedPlayer = random.choice(players)
        gapOfMMR = assignedPlayer[1] - player1[1]
        # set the player with higher MMR value as player1, lower one as player2
        if gapOfMMR >= 0:
            player2 = player1
            player1 = assignedPlayer
        else:
            player2 = assignedPlayer
        # print(player1, player2)

        # randomly assigned battle conditions judgement
        if match_conditions_judgement(player1, player2):
            # battle
            winner = game_play(player1, player2)
        else:
            continue

        # update battle results
        if winner == 1:
            numOfWin = player1[0]
            numOfLost = player2[0]

            # update MMR values
            players[numOfWin][1] += changeMMR
            if players[numOfLost][1] - changeMMR < 0:
                players[numOfLost][1] = 0
            else:
                players[numOfLost][1] -= changeMMR

            # update battle record
            players[numOfWin][2] += 1
            players[numOfWin][3] += 1

            players[numOfLost][2] += 1
            players[numOfLost][4] += 1

        elif winner == 2:
            numOfWin = player2[0]
            numOfLost = player1[0]

            # update the MMR values
            players[numOfWin][1] += changeMMR
            if players[numOfLost][1] - changeMMR < 0:
                players[numOfLost][1] = 0
            else:
                players[numOfLost][1] -= changeMMR

            # update battle record
            players[numOfWin][2] += 1
            players[numOfWin][3] += 1

            players[numOfLost][2] += 1
            players[numOfLost][4] += 1

    return players

def match_conditions_judgement(player1: list, player2: list):
    '''
    To determine whether the assigned match meet the following two requirements.
    If not, the match would proceed. If yes, the match would not proceed.
    :param player1: the selected player1 in the assigned match
    :param player2: the selected player2 in the assigned match
    :return: if the match would proceed, return True. If the match
    would not proceed, then return False
    '''
    if player1[0] == player2[0]:
        return False
    elif abs(player1[1] - player2[1]) >= battleMMRgap:
        return False
    else:
        return True

def game_play(player1: list, player2: list):
    '''
    Two selected players would battle through this game. At first, player1 would
    take number 0 - 5000, and player2 would take number 5001 - 10000. Secondly,
    compensation would be given to the player with higher MMR points. Thirdly, a
    random number within 0 - 10000 would be generated. Then if player1 contains
    this number, player1 would be the winner.
    :param player1: selected player1
    :param player2: selected player2
    :return: return 1 or 2, 1 means that player1 wins, 2 means that player2 wins
    '''
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

if __name__ == '__main__':
    players = generate_players(30000)

    for i in range(2000):
        players = assign_players_match(players)

    x = []
    y = []
    for j in range(len(players)):
        x.append(players[j][0])
        y.append(players[j][1])

    plt.scatter(x, y)
    plt.show()