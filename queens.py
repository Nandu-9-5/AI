def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens_util(board, col, N, solutions):
    # If all queens are placed, add this solution
    if col >= N:
        solutions.append([row[:] for row in board])
        return

    # Place queen in each row one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen
            board[i][col] = "Q"

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1, N, solutions)

            # If placing queen doesn't lead to a solution, backtrack
            board[i][col] = "."

def solve_n_queens(N):
    board = [["." for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)

    if solutions:
        print(f"Total solutions for {N}-Queens: {len(solutions)}\n")
        for idx, solution in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            print_board(solution)
    else:
        print("No solution exists")

# Example usage:
N = int(input("Enter the number of queens: "))
solve_n_queens(N)
