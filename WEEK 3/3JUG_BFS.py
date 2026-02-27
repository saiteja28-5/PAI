from collections import deque
def bfs_3_jug(cap, target):
    A, B, C = cap
    start = (0, 0, 0)
    q = deque([(start, [])])
    vis = {start}
    while q:
        (x, y, z), path = q.popleft()
        if (x, y, z) == target:
            return path + [(x, y, z)]
        states = {
            (A,y,z), (x,B,z), (x,y,C),
            (0,y,z), (x,0,z), (x,y,0),
            (x-min(x,B-y), y+min(x,B-y), z),
            (x-min(x,C-z), y, z+min(x,C-z)),
            (x+min(y,A-x), y-min(y,A-x), z),
            (x, y-min(y,C-z), z+min(y,C-z)),
            (x+min(z,A-x), y, z-min(z,A-x)),
            (x, y+min(z,B-y), z-min(z,B-y))
        }
        for s in states:
            if s not in vis:
                vis.add(s)
                q.append((s, path + [(x,y,z)]))
    return None
capacities = (8, 5, 3)
target = (4, 4, 0)
result = bfs_3_jug(capacities, target)
if result:
    print("Solution steps:")
    for step in result:
        print(step)
else:
    print("No solution found")
