import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  p = input().rstrip()
  n = int(input())
  if n == 0:
    k = input()
    L = []
  else:
    L = list(map(int, input().rstrip()[1:-1].split(',')))
  l = 0
  r = n-1
  Re = False
  e = False
  
  for x in p:
    if x == 'R':
      Re = not Re

    if x == 'D':
      if r < l :
        e = True
        break
      if Re:
        r -= 1
      else:
        l += 1
        
  if e:
    print('error')
  else:
    if r<l:
      print('[]')
    elif Re:
      if l == 0:
        print('[',','.join(map(str,L[r::-1])),']',sep = '')
      else:
        print('[',','.join(map(str,L[r:l-1:-1])),']',sep = '')
    else:
      print('[',','.join(map(str,L[l:r+1])),']',sep = '')
      
      