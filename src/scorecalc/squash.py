'''
Created on 15 Mar 2012

@author: Mark Hearn
'''

import csv


def calculateScore(a, b):
    '''Calculates best-of-five squash points with a total of 7

    @param a: the number of games won by player a
    @param b: the number of games won by player b
    '''
    if a == 3:
        aScore, bScore = 6 - b, b + 1
    elif b == 3:
        aScore, bScore = a + 1, 6 - a
    else:
        aScore, bScore = a + 1, b + 1
    return aScore, bScore


data = csv.reader(open('/home/mark/squash/bas.csv', 'rb'))
rowNumber, aTotalScore, bTotalScore = 1, 0, 0
for row in data:
    if rowNumber == 1:
        aName, bName = row[0], row[1]
        rowNumber = 2
    else:
        a, b = int(row[0]), int(row[1])
        aScore, bScore = calculateScore(a, b)
        aTotalScore, bTotalScore = aTotalScore + aScore, bTotalScore + bScore

print aName, aTotalScore, "-", bTotalScore, bName
