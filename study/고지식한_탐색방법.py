p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)

def BF(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == M : return i-M
    else : return -1

print(BF(p, t))