from collections import deque
f=((1,2,3),(4,5,6),(7,8,0))
d=[(-1,0),(1,0),(0,-1),(0,1)]
def p(x,k):
 print(k)
 for r in x:print(*r)
def a(b,r,c):
 s=tuple(tuple(r) for r in b);q=deque([(s,r,c,0)]);v={s}
 while q:
  curr,y,x,z=q.popleft();p(curr,z)
  if curr==f:print(z);return
  for dy,dx in d:
   ny,nx=y+dy,x+dx
   if 0<=ny<3 and 0<=nx<3:
    t=[list(r) for r in curr];t[y][x],t[ny][nx]=t[ny][nx],t[y][x];n=tuple(tuple(r) for r in t)
    if n not in v:v.add(n);q.append((n,ny,nx,z+1))
b=[[1,2,3],[4,0,5],[6,7,8]]
a(b,1,1)
