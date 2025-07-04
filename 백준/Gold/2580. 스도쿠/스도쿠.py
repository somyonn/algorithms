L = []
s = []

for i in range(9):
  L.append(list(map(int, input().split())))

for i in range(9):
  for j in range(9):
    if L[i][j] == 0:
      s.append([i,j])

def row(i,k):
  for x in range(9):
    if L[i][x] == k:
      return False
  return True

def col(j,k):
  for x in range(9):
    if L[x][j] == k:
      return False
  return True

def sqr(i,j,k):
  for x in range(i//3*3, i//3*3+3):
    for y in range(j//3*3, j//3*3+3):
      if L[x][y] == k:
        return False
  return True

def dfs(m):
  if len(s) == m:
    for i in L:
      for j in i:
        print(j, end = ' ')
      print()
    exit(0)
  else:
    for k in range(1,10):
      i = s[m][0]
      j = s[m][1]

      if row(i,k) and col(j,k) and sqr(i,j,k):
        L[i][j] = k
        dfs(m+1)
        L[i][j] = 0
  
dfs(0)      