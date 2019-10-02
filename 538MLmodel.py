import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import csv
from sklearn.utils import shuffle
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style

data = pd.read_csv('/Users/alexchandy13/Downloads/condensed538data.csv', sep=",")
print(data.head())

predict = 'correct?'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

lm = linear_model.LinearRegression()
lm.fit(x_train,y_train)
acc = lm.score(x_test,y_test)

print("Score: ", lm.score(x_test,y_test))
print("y = ", lm.intercept_," + ", lm.coef_,"x")

dfr = open('/Users/alexchandy13/Downloads/nfl-elo/nfl_elo.csv', 'r')
fgames = []

for row in csv.reader(dfr):
    fgame = []
    if row[1] == '2019' and row[6] != '' and row[10] == '':
        def dateParse(date):
            dates = date.split('/')
            m = int(dates[0])
            d = int(dates[1])
            y = 2000 + int(dates[2])
            return 10000 * y + 100 * m + d
        fgame.append(dateParse(row[0]))
        fgame.append(int(row[1]))
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
        fgame.append(teamID(row[4]))
        fgame.append(teamID(row[5]))
        for i in range(6, 10):
            fgame.append(float(row[i]))
        for i in range(16, 22):
            fgame.append(float(row[i]))
    if len(fgame) != 0:
        fgames.append(fgame)

print(lm.predict(fgames))
