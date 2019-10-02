import csv

dfr = open('/Users/alexchandy13/PycharmProjects/bettingML/nfl_elo.csv', 'r')

count = 0
games = []
for row in csv.reader(dfr):
    count += 1
    game = []
    if count > 1:
        if int(row[1]) > 1999 and int(row[1]) < 2019:
            def dateParse(date):
                dates = date.split('/')
                m = int(dates[0])
                d = int(dates[1])
                y = 2000 + int(dates[2])
                return 10000 * y + 100 * m + d
            game.append(dateParse(row[0]))
            game.append(int(row[1]))
            def teamID(team):
                if team == 'ARI':
                    return 1
                elif team == 'ATL':
                    return 2
                elif team == 'BAL':
                    return 3
                elif team == 'BUF':
                    return 4
                elif team == 'CAR':
                    return 5
                elif team == 'CHI':
                    return 6
                elif team == 'CIN':
                    return 7
                elif team == 'CLE':
                    return 8
                elif team == 'DAL':
                    return 9
                elif team == 'DEN':
                    return 10
                elif team == 'DET':
                    return 11
                elif team == 'GB':
                    return 12
                elif team == 'HOU':
                    return 13
                elif team == 'IND':
                    return 14
                elif team == 'JAX':
                    return 15
                elif team == 'KC':
                    return 16
                elif team == 'LAC':
                    return 17
                elif team == 'LAR':
                    return 18
                elif team == 'MIA':
                    return 19
                elif team == 'MIN':
                    return 20
                elif team == 'NE':
                    return 21
                elif team == 'NO':
                    return 22
                elif team == 'NYG':
                    return 23
                elif team == 'NYJ':
                    return 24
                elif team == 'OAK':
                    return 25
                elif team == 'PHI':
                    return 26
                elif team == 'PIT':
                    return 27
                elif team == 'SEA':
                    return 28
                elif team == 'SF':
                    return 29
                elif team == 'TB':
                    return 30
                elif team == 'TEN':
                    return 31
                elif team == 'WSH':
                    return 32
            game.append(teamID(row[4]))
            game.append(teamID(row[5]))
            for i in range(6,10):
                game.append(float(row[i]))
            for i in range(16,22):
                game.append(float(row[i]))
            s1 = int(row[28])
            s2 = int(row[29])
            p1 = float(row[20])
            p2 = float(row[21])
            diff = abs(p1-p2)
            if p1 > p2 and s1 > s2:
                game.append(1)
            elif p1 < p2 and s1 < s2:
                game.append(1)
            else:
                game.append(0)

    if not len(game) == 0:
        games.append(game)

dfw = open('/Users/alexchandy13/PycharmProjects/bettingML/condensed538data.csv', 'w')

csv.writer(dfw).writerow(['date','season','hometeam','awayteam','elo1_pre','elo2_pre',
                          'elo_prob1','elo_prob2',
                          'qb1_value_pre','qb2_value_pre','qb1_adj','qb2_adj',
                          'qbelo_prob1','qbelo_prob2','correct?'])
for game in games:
    csv.writer(dfw).writerow(game)

dfw.close()