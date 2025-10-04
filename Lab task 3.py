from collections import deque
# Each state is represented as (x, y)
# x = amount in 4-gal jug
# y = amount in 3-gal jug

def get_next_states(x, y):
    states = []

    # 1. Fill 4-gal jug
    if x < 4:
        states.append((4, y))
    
    # 2. Fill 3-gal jug
    if y < 3:
        states.append((x, 3))
    
    # 3. Empty 4-gal jug
    if x > 0:
        states.append((0, y))
    
    # 4. Empty 3-gal jug
    if y > 0:
        states.append((x, 0))
    
    # 5. Pour from 3-gal into 4-gal
    if x + y >= 4 and y > 0:
        states.append((4, y - (4 - x)))
    
    # 6. Pour from 4-gal into 3-gal
    if x + y >= 3 and x > 0:
        states.append((x - (3 - y), 3))
    
    # 7. Pour all from 3-gal into 4-gal (if it fits)
    if x + y <= 4 and y > 0:
        states.append((x + y, 0))
    
    # 8. Pour all from 4-gal into 3-gal (if it fits)
    if x + y <= 3 and x > 0:
        states.append((0, x + y))
    
    return states


def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))  # state, path
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        # Goal check
        if (x, y) == goal:
            return path

        # Expand next states
        for nx, ny in get_next_states(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None

if __name__ == "__main__":
    start_state = (0, 0)
    goal_state = (2, 0)
    solution_path = bfs(start_state, goal_state)

    if solution_path:
        print("Solution path:")
        for state in solution_path:
            print(state)
    else:
        print("No solution found.")
        
      