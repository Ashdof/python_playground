#!/usr/bin/python3
"""A demonstration of floddfill in a paint application"""

import sys

# create image
im = [list('..########################...........'),
        list('..#......................#...#####...'),
        list('..#..........########....#####...#...'),
        list('..#..........#......#............#...'),
        list('..#..........########.........####...'),
        list('..######......................#......'),
        list('.......#..#####.....###########......'),
        list('.......####...#######................')]

HEIGHT = len(im)
WIDTH = len(im[0])


def floodfill(image, x, y, newChar, oldChar = None):
    if oldChar == None:
        #oldChar defaults to character at x, y
        oldChar = image[y][x]
    
    if oldChar == newChar or image[y][x] != oldChar:
        #base case
        return

    image[y][x] = newChar # change the character

    printImage(image)

    #change the neighbouring characters
    if y + 1 < HEIGHT and image[y + 1][x] == oldChar:
        # recursive case
        floodfill(image, x, y + 1, newChar, oldChar)

    if y - 1 >= 0 and image[y - 1][x] == oldChar:
        # recursive case
        floodfill(image, x, y - 1, newChar, oldChar)
    
    if x + 1 < WIDTH and image[y][x + 1] == oldChar:
        # recursive case
        floodfill(image, x + 1, y, newChar, oldChar)

    if x - 1 >= 0 and image[y][x - 1] == oldChar:
        # recursive case
        floodfill(image, x - 1, y, newChar, oldChar)

    return  #base case

def printImage(image):
    for y in range(HEIGHT):
        # print each row
        for x in range(WIDTH):
            #print each column
            sys.stdout.write(image[y][x])
        sys.stdout.write('\n')
    sys.stdout.write('\n')



#   ======================================================

if __name__ == '__main__':

    printImage(im)
    floodfill(im, 3, 3, '0')
    printImage(im)
