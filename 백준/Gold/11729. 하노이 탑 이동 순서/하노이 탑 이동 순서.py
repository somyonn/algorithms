import sys
input = sys.stdin.readline

N = int(input())

s = 0
L = []

def Hanoi(N, p, q):
    global L
    global s
    if N == 1:
        s+= 1
        L.append([p, q])
    else:
        Hanoi(N-1, p, 6-p-q)
        L.append([p, q])
        s+= 1
        Hanoi(N-1, 6-p-q, q)

Hanoi(N, 1, 3)

print(s)
for i in L:
    for j in i:
        print(j, end = ' ')
    print()
    
        
    
    
    