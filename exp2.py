from collections import deque
def is_goal(state, goal):
    return goal == state
def get_next_states(state, j1_capacity, j2_capacity):
    j1, j2 = state
    states = []
    states.append((j1_capacity, j2)) 
    states.append((j1, j2_capacity)) 
    states.append((0, j2))
    states.append((j1, 0))            
    pour = min(j1, j2_capacity - j2)
    states.append((j1 - pour, j2 + pour))
    pour = min(j2, j1_capacity - j1)
    states.append((j1 + pour, j2 - pour))
    return states
def water_jug_bfs(j1_capacity, j2_capacity, init_state, goal_state):
    visited = set()
    queue = deque([(init_state, [])])  
    while queue:
        state, path = queue.popleft()
        if is_goal(state, goal_state):
            return path + [state]
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_next_states(state, j1_capacity, j2_capacity):
            if next_state not in visited:
                queue.append((next_state, path + [state]))
    
    return None
j1_capacity = int(input("Enter Jug1 capacity: "))
j2_capacity = int(input("Enter Jug2 capacity: "))
init_j1 = int(input("Enter initial amount in Jug1: "))
init_j2 = int(input("Enter initial amount in Jug2: "))
init_state = (init_j1, init_j2)
goal_j1 = int(input("Enter goal amount in Jug1: "))
goal_j2 = int(input("Enter goal amount in Jug2: "))
goal_state = (goal_j1, goal_j2)
result = water_jug_bfs(j1_capacity, j2_capacity, init_state, goal_state)
if result:
    for step in result:
        print(step)
else:
    print("No Solution found")
