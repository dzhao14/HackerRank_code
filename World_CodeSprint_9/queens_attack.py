#https://www.hackerrank.com/contests/world-codesprint-9/challenges/queens-attack-2

def queen_squares(n, queenR, queenC, ob_list):
    closeR = n - queenC
    closeL = queenC - 1
    closeU = n - queenR
    closeD = queenR - 1
    closeRU = min(closeR, closeU)
    closeLU = min(closeL, closeU)
    closeDR = min(closeR, closeD)
    closeDL = min(closeL, closeD)
    
    for tup in ob_list:
        r = tup[0]
        c = tup[1]
        #right
        if r == queenR and c > queenC:
            if c - queenC - 1 < closeR:
                closeR = c - queenC - 1
        #left
        elif r == queenR and c < queenC:
            if queenC - c - 1 < closeL:
                closeL = queenC - c - 1
        #up
        elif c == queenC and r > queenR:
            if r - queenR - 1 < closeU:
                closeU = r - queenR - 1
        #down
        elif c == queenC and r < queenR:
            if queenR - r - 1 < closeD:
                closeD = queenR - r - 1
        #RU
        elif c-queenC == r-queenR and r > queenR:
            if r - queenR - 1 < closeRU:
                closeRU = r - queenR - 1
        #DL
        elif c-queenC == r-queenR and r < queenR:
            if queenR - r  - 1 < closeDL:
                closeDL = queenR - r - 1
        #LU
        elif c+r == queenR+queenC and c < queenC:
            if queenC - c - 1 < closeLU:
                closeLU = queenC - c - 1
        #DR
        elif c+r == queenR+queenC and c > queenC:
            if c - queenC - 1 < closeDR:
                closeDR = c - queenC - 1
        else:
            pass

    return closeR + closeL + closeU + closeD + closeRU + closeDL + closeLU + closeDR
            
            

if __name__ == '__main__':
    board_obstacles = input()
    bolist = board_obstacles.split()
    n = int(bolist[0])
    k = int(bolist[1])
    queen_loc = input()
    queenlist = queen_loc.split()
    queenR = int(queenlist[0])
    queenC = int(queenlist[1])

    ob_list = []
    for x in range(0, k):
        ob = input()
        obtup = ob.split()
        obtup = tuple(map(int, obtup))
        ob_list.append(obtup)

    count = queen_squares(n, queenR, queenC, ob_list)
    print(count)
