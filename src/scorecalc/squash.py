'''
Created on 15 Mar 2012

@author: Mark Hearn
'''

import sys
import csv
from optparse import OptionParser


def main():
    parser = OptionParser(usage="USAGE: %prog [options] filename")
    parser.add_option("-t", "--total",
                      action="store_true",
                      dest="total",
                      default=False,
                      help="calculate the total score")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        print "Only one argument permitted.\n\
        Usage: %prog [options] filename"
        sys.exit()
    if options.total == True:
        calculateTotalScore()


def calculateMatchScore(a, b):
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


def calculateTotalScore():
    """Calculates the total score over the whole file
    """
    data = csv.reader(open(sys.argv[-1], 'rb'))
    rowNumber, aTotalScore, bTotalScore = 1, 0, 0
    for row in data:
        if rowNumber == 1:
            aName, bName = row[0], row[1]
            rowNumber = 2
        else:
            a, b = int(row[0]), int(row[1])
            aScore, bScore = calculateMatchScore(a, b)
            aTotalScore, bTotalScore = \
            aTotalScore + aScore, bTotalScore + bScore
    print "Total score:", aName, aTotalScore, "-", bTotalScore, bName

if __name__ == '__main__':
    main()
