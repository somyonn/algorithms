import sys, math
input = sys.stdin.readline

x = int(input())

L = [[' ' for _ in range(x)] for _ in range(x)]

def star(x, p, q):
    
    global L
    if x != 3:
        x //= 3
        for i in range(p, p+3*x, x):
            for j in range(q, q+3*x, x):
                if i != p+x or j != q+x :
                    star(x, i, j)
    else:
        for i in range(p, p+3):
            for j in range(q, q+3):
                if i != p+1 or j != q+1 :
                    L[i][j] = '*'

star(x, 0, 0)

for i in L:
    for j in i:
        print(j, end = '')
    print()