#!/usr/bin/python3

import sys

# set up towers A, B, and C. The end of the list is the top of the tower
TOTAL_DISKS = 9

#populate twoer A:
TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS + 1))), 'B': [], 'C': []}

def printDisk(diskNum):
    # print a single disk of width diskNum
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)

    if diskNum == 0:
        # just draw the pole
        sys.stdout.write(emptySpace + '||' + emptySpace)
    else:
        # draw the disk
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        sys.stdout.write(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace)

def printTowers():
    # print all three towers

    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        sys.stdout.write('\n')

    # print the tower labels A, B, C
    emptySpace = ' ' * (TOTAL_DISKS)
    print("%s A%s%s B%s%s C\n" % (emptySpace, emptySpace, emptySpace, emptySpace, emptySpace))

def moveOneDisk(startTower, endTower):
    # move the top disk from the start tower to the end tower
    disk = TOWERS[startTower].pop()
    TOWERS[endTower].append(disk)

def solve(numberOfDisks, startTower, endTower, tempTower):
    # move the top numberOfDisks disk from startTower to endTower

    if numberOfDisks == 1:
        # base case
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        # recursive case
        solve(numberOfDisks - 1, startTower, tempTower, endTower)
        moveOneDisk(startTower, endTower)
        solve(numberOfDisks - 1, tempTower, endTower, startTower)
        return



#   ======================================================================

if __name__ == '__main__':

    printTowers()
    solve(TOTAL_DISKS, 'A', 'B', 'C')

    while True:
        printTowers()
        print("Enter letter of start tower and end tower.  (A, B, C) or Q to quit")
        move = input().upper()
        if move == 'Q':
            sys.exit()
        elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
            moveOneDisk(move[0], move[1])
