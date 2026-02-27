def dfs_3_jug(cap, target):
    A, B, C = cap
    start = (0, 0, 0)
    visited = set()

    def dfs(state, path):
        if state in visited:
            return None
        visited.add(state)

        x, y, z = state
        path = path + [state]

        if state == target:
            return path

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
            result = dfs(s, path)
            if result:
                return result
        return None

    return dfs(start, [])


# ---------- MAIN ----------
capacities = (8, 5, 3)
target = (4, 4, 3)

result = dfs_3_jug(capacities, target)

if result:
    print("DFS Solution:")
    for step in result:
        print(step)
else:
    print("No solution found")
