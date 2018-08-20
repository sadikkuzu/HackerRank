# https://www.hackerrank.com/challenges/the-minion-game

def minion_game(string):
    # your code goes here
    n = len(string)
    S = string
    vows = ['A', 'E', 'I', 'O', 'U']
    stus = kevs = 0
    for i in xrange(n):
        if S[i] in vows:
            kevs += n-i
        else:
            stus += n-i
    if stus>kevs:
        print "Stuart", stus
    elif kevs>stus:
        print "Kevin", kevs
    else:
        print "Draw"