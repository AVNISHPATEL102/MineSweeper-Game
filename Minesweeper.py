import random
import sys

grid = [[None for _ in range(8)] for _ in range(8)]
count=0
while True:
    r=random.randint(0,7)
    c=random.randint(0,7)
    if(grid[r][c] == None):
        grid[r][c] = 'M'
        count+=1
    if(count >=10):
        break

for r in range(8):
    for c in range(8):
        temp=0
        if grid[r][c] != 'M':
            if (r-1) >=0 and (c-1) >=0 :
                if(grid[r-1][c-1] == 'M'):
                    temp+=1
            if (r-1) >=0:
                if(grid[r-1][c] == 'M'):
                    temp+=1
            if(r-1) >=0 and (c+1) <=7:
                if(grid[r-1][c+1] == 'M'):
                    temp+=1
            if((c-1) >=0 ):
                if(grid[r][c-1] == 'M'):
                    temp+=1
            if((c+1)<=7):
                if(grid[r][c+1] == 'M'):
                    temp+=1
            if(r+1) <=7 and (c-1) >=0:
                if grid[r+1][c-1] == 'M':
                    temp+=1
            if (r+1) <= 7:
                if grid[r+1][c] == 'M':
                    temp+=1
            if (r+1) <= 7 and (c+1) <= 7 :
                if grid[r+1][c+1] == 'M':
                    temp+=1
            grid[r][c]=temp



for r in range(8):
    for c in range(8):
        print(grid[r][c],end="\t")
    print(" ")

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


playergrid = [[None for _ in range(8)] for _ in range(8)]

for r in range(8):
    for c in range(8):
        playergrid[r][c]='S'

for r in range(9):
    if r ==0:
        print("",end="\t")
    else:
        print("{}".format((r-1)),end="\t")
print("")

for r in range(8):
    print("{}".format(r),end="\t")
    for c in range(8):
        print(playergrid[r][c],end="\t")
    print(" ")

def board(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co] = gr[ro][co]
    elif cl == 0:
        plgr[ro][co] = gr[ro][co]
        if (co - 1) >= 0:
            leftmid(gr,plgr,gr[ro][co-1],(ro),(co-1))
        if (co + 1) <= 7:
            rightmid(gr,plgr,gr[ro][co+1],(ro),(co+1))
        if (ro- 1) >= 0:
            upmid(gr,plgr,gr[ro-1][co],(ro-1),(co))
        if (ro + 1) <= 7:
            downmid(gr,plgr,gr[ro+1][co],(ro+1),(co))
        if (ro - 1) >= 0 and (co + 1) <= 7:
            uprightcorner(gr, plgr, gr[ro - 1][co + 1], (ro - 1), (co + 1))
        if (ro-1) >= 0 and (co-1) >= 0:
            upleftcorner(gr,plgr,gr[ro-1][co-1],(ro-1),(co-1))
        if (ro+1) <= 7 and (co-1) >= 0:
            bottomleftcorner(gr,plgr,gr[ro+1][co-1],(ro+1),(co-1))
        if (ro+1) <= 7 and (co+1) <= 7:
            bottomrightcorner(gr,plgr,gr[ro+1][co+1],(ro+1),(co+1))


def leftmid(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (co - 1) >= 0:
            leftmid(gr,plgr,gr[ro][co-1],(ro),(co-1))


def rightmid(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (co + 1) <= 7:
            rightmid(gr,plgr,gr[ro][co+1],(ro),(co+1))


def upmid(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (ro- 1) >= 0:
            upmid(gr,plgr,gr[ro-1][co],(ro-1),(co))


def downmid(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (ro + 1) <= 7:
            downmid(gr,plgr,gr[ro+1][co],(ro+1),(co))


def uprightcorner(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (ro - 1) >= 0:
            upmid(gr,plgr,gr[ro-1][co],(ro-1),co)
        if (ro-1) >= 0 and (co+1) <= 7:
            uprightcorner(gr,plgr,gr[ro-1][co+1],(ro-1),(co+1))
        if (co+1) <= 7:
            rightmid(gr,plgr,gr[ro][co+1],ro,(co+1))


def upleftcorner(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (ro - 1) >= 0:
            upmid(gr,plgr,gr[ro-1][co],(ro-1),co)
        if (ro-1) >= 0 and (co-1) >= 0:
            upleftcorner(gr,plgr,gr[ro-1][co-1],(ro-1),(co-1))
        if (co-1) >=0:
            leftmid(gr,plgr,gr[ro][co-1],ro,(co-1))


def bottomleftcorner(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (ro + 1) >= 0:
            downmid(gr,plgr,gr[ro+1][co],(ro+1),co)
        if (ro+1) <= 7 and (co-1) >= 0:
            bottomleftcorner(gr,plgr,gr[ro+1][co-1],(ro+1),(co-1))
        if (co-1) >=0:
            leftmid(gr,plgr,gr[ro][co-1],ro,(co-1))


def bottomrightcorner(gr,plgr,cl,ro,co):
    if cl != 0 and cl != 'M':
        plgr[ro][co]=gr[ro][co]
    elif cl == 0:
        plgr[ro][co]=gr[ro][co]
        if (ro + 1) >= 0:
            downmid(gr,plgr,gr[ro+1][co],(ro+1),co)
        if (ro+1) <= 7 and (co+1) <= 7:
            bottomrightcorner(gr,plgr,gr[ro+1][co+1],(ro+1),(co+1))
        if (co + 1) <= 7:
            rightmid(gr, plgr, gr[ro][co + 1], ro, (co + 1))


while True:
    r = int(input("Please enter the row number of the cell you want to select"))
    while r < 0 or r > 7:
        r = int(input("Please enter the row number of the cell you want to select. "
                      "Your selection should be valid and between 0 to 7"))
    c = int(input("Please enter the column number of the cell you want to select"))
    while c < 0 or c > 7:
        c = int(input("Please enter the column number of the cell you want to select. "
                      "Your selection should be valid and between 0 to 7"))
    cell = grid[r][c]
    if cell == 'M':
        sys.exit("You put your foot on a MINE you lost")

    board(grid,playergrid,cell,r,c)
    print("")
    print("")
    print("")
    print("")
    for i in range(9):
        if i == 0:
            print("", end="\t")
        else:
            print("{}".format((i - 1)), end="\t")
    print("")

    for i in range(8):
        print("{}".format(i), end="\t")
        for j in range(8):
            print(playergrid[i][j], end="\t")
        print(" ")










