import os
import pyganim
import pygame

def getPygAnimListFromDir(dirpath, delay):
    res = []

    for a in os.listdir(dirpath):
        s = dirpath+'/'+a
        if os.path.isfile(s):
            res.append((s, delay))
        # print(s)

    return res
def getImagesFromSpriteSheet(filename, startX, startY, width, height, rows, cols):
    x = startX
    y = startY
    res = []
    for i in range(0, rows):
        for j in range(0, cols):
            rect = (x,y,width,height)
            res.append(rect)
            x += width
        x = startX
        y += height
    
    return pyganim.getImagesFromSpriteSheet(filename, rects=res)

# path = os.path.dirname(__file__)+'/img/coins/1'
# animList = getPygAnimListFromDir(path, 100)
# print(animList)
if __name__ == "__main__":
    a = getImagesFromSpriteSheet('platformer/img/character/run/1x.png',0,0,100,100,1,10)
    print(a)
