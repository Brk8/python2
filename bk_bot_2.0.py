#bk bot 2.0 team picks 2023-2024 season
#update wk variable for whatever week picking for

import pandas as pd
import xlrd
import random

game1 = []
game2 = []
game3 = []
games = []
schedule = pd.read_csv('C:\\Users\\bkent\\OneDrive\\Desktop\\nfl_schedule.txt')
wk = 'WEEK18'



def random_choice(schedule_week):

    """ function to accept new week choice and pass parameter to filter"""

    #pass in parameter to filter down table
    wk_games = schedule[schedule.WEEK == schedule_week]

    #take 3 random games
    top3 = wk_games.sample(n=3)

    print(top3,"\n")

    #iterate through rows and append teams columns to list
    for index, rows in top3.iterrows():
        for_list = [rows.TEAM_1,rows.TEAM_2]
        games.append(for_list)



    #append games to separate lists
    game1.append(games[0])
    game2.append(games[1])
    game3.append(games[2])


    #pick random choice for each game
    print("Game 1 pick is: ")
    for sublist in game1:
        print(random.choice(sublist))


    print("Game 2 pick is: ")
    for sublist in game2:
        print(random.choice(sublist))


    print("Game 3 pick is: ")
    for sublist in game3:
        print(random.choice(sublist))




random_choice(wk)

