#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for idx,row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            bot = (idx, row.index('m'))
            
    row_val = princess[0] - bot[0] #if negative then up
    col_val = princess[1] - bot[1] #if negative then left
    
    return ''.join([
    'UP\n' * abs(row_val) if row_val < 0 else 'DOWN\n'* abs(row_val),
    'LEFT\n'*abs(col_val) if col_val < 0 else 'RIGHT\n'* abs(col_val)])
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

result = displayPathtoPrincess(m,grid)
print(result)
