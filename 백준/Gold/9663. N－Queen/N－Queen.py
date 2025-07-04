N = int(input())

L = [0]*N
s = 0

def check(x):
  for i in range(x):
    if L[x] == L[i] or L[i] == L[x] - (x-i) or L[i] == L[x] + (x-i) : return False

  return True
    

def Q(x):
  global s
  if x == N:
    s += 1
    return
  
  for i in range(N):
    L[x] = i
    if check(x):
      Q(x+1)

Q(0)
print(s)