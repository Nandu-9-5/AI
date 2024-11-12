from collections import deque

def get_initial_state():
    monkey_pos = input("Enter the monkey's initial position (floor, corner, middle): ").strip().lower()
    box_pos = input("Enter the box's initial position (corner, middle, under_banana): ").strip().lower()
    return {
        "monkey_pos": monkey_pos,
        "box_pos": box_pos,
        "has_banana": False
    }

def move(state, destination):
    return {**state, "monkey_pos": destination}

def push_box(state, destination):
    return {**state, "monkey_pos": destination, "box_pos": destination}

def climb_box(state):
    if state["monkey_pos"] == state["box_pos"]:
        return {**state, "monkey_pos": "on_box"}
    return state

def grab_banana(state):
    if state["monkey_pos"] == "on_box":
        return {**state, "has_banana": True}
    return state

def monkey_banana_bfs(initial_state):
    goal_state = ("has_banana", True)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        state_tuple = (
            current_state["monkey_pos"],
            current_state["box_pos"],
            current_state["has_banana"]
        )

        if state_tuple in visited:
            continue

        visited.add(state_tuple)
        if current_state["has_banana"]:
            return path

        # Define possible actions
        actions = [
            ("move to middle", move(current_state, "middle")),
            ("move to corner", move(current_state, "corner")),
            ("push box to under banana", push_box(current_state, "under_banana")),
            ("climb box", climb_box(current_state)),
            ("grab banana", grab_banana(current_state))
        ]

        # Explore each action
        for action, new_state in actions:
            if new_state != current_state:
                queue.append((new_state, path + [action]))

    return None

initial_state = get_initial_state()
solution = monkey_banana_bfs(initial_state)
if solution:
    print("Solution found!")
    for step in solution:
        print(step)
else:
    print("No solution found.")
