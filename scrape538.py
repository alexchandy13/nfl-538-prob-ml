import requests
from bs4 import BeautifulSoup
import csv

for year in range(7, 9):
    URL = ('https://projects.fivethirtyeight.com/201%d-nfl-predictions/games/' % year)
    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')

    datalist = []

    for logo in soup.find_all("td", attrs={"class": "td logo"}):
        for sib in logo.find_next_siblings('td'):
            datalist.append(sib.contents)

    matchups = []

    i = 0
    while i < len(datalist):
        matchup = []
        for j in range(8):
            datum = datalist[i + j][0]
            matchup.append(datum)
        matchups.append(matchup)
        i = i + 8

    bins = []
    for b in range(10):
        bins.append([0,0])

    p0 = 0
    count = 0
    while p0 <= 100:
        for i in matchups:
            s1 = int(i[3])
            s2 = int(i[7])
            p1 = int(i[2].replace('%', ''))
            p2 = int(i[6].replace('%', ''))
            diff = abs(p1-p2)
            if diff < p0 + 10 and diff >= p0:
                bins[count][1] = bins[count][1] + 1
                if p1 > p2 and s1 > s2:
                    bins[count][0] = bins[count][0] + 1
                if p1 < p2 and s1 < s2:
                    bins[count][0] = bins[count][0] + 1
        p0 = p0 + 10
        count = count + 1

    for bin in bins:
        if bin[1] == 0:
            bin.append(0)
        else:
            bin.append(bin[0]/bin[1])

    dfw = open(('/Users/alexchandy13/PycharmProjects/bettingML/scrape201%dpred.csv' % year), 'w')

    for bin in bins:
        csv.writer(dfw).writerow(bin)

    dfw.close()





