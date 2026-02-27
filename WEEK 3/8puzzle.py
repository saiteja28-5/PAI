from heapq import *

G=((1,2,3),(4,5,6),(7,8,0))

h=lambda s:sum(abs(i-(v-1)//3)+abs(j-(v-1)%3)
    for i in range(3) for j,v in enumerate(s[i]) if v)

def N(s):
    i,j=[(i,j) for i in range(3) for j in range(3) if s[i][j]==0][0]
    for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=i+x<3 and 0<=j+y<3:
            t=[list(r) for r in s]
            t[i][j],t[i+x][j+y]=t[i+x][j+y],t[i][j]
            yield tuple(map(tuple,t))

def A(start):
    q=[(h(start),0,start,[start])]
    seen=set()
    while q:
        f,g,s,p=heappop(q)
        if s==G: return p
        if s in seen: continue
        seen.add(s)
        for n in N(s):
            heappush(q,(g+1+h(n),g+1,n,p+[n]))

S=((1,2,3),(4,0,6),(7,5,8))
for step in A(S):
    print(step)