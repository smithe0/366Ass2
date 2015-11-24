numTilings = 8
offset = (0.6/8)
tileWidth = 0.6

#import numpy as np

#        X = x + (i*offset); Y = y + (i*offset)
#       X = int(x/0.6); Y = int(y/0.6)

def tilecode(x,y,tileIndices):
    for i in range(0,numTilings):
        X = int(x/0.6); Y = int(y/0.6)
        index = ((Y*11)+X)+(121*i)
        tileIndices[i] = index
        x=x+offset; y=y+offset
    
def printTileCoderIndices(x,y):
    tileIndices = [-1]*numTilings
    tilecode(x,y,tileIndices)
    print 'Tile indices for input (',x,',',y,') are : ', tileIndices

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
    
