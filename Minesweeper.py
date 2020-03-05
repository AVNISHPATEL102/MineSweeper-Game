import random

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


for r in range(8):
    for c in range(8):
        print(playergrid[r][c],end="\t")
    print(" ")












