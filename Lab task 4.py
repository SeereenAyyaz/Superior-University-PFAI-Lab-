def print_board(board, n):
   #Printing the chessboard with queen's positions.
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += " Q "
            else:
                row += " . "
        print(row)
    print("\n")

def is_safe(board, row, col):
    #Checking if placing a queen at (row, col) is safe or not.
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n):
   # I'm doing recursive function to solve N-Queens using backtracking here.
    if row == n:
        print("Solution Found:")
        print_board(board, n)
        return True

    found = False
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            found = solve_n_queens(board, row + 1, n) or found
    return found
def n_queens():
    n = int(input("Enter the number of queens (N): "))
    board = [-1] * n  # -1 here is indicating that no queen is placed in that row yet
    print(f"\nSolving {n}-Queens Problem...\n")
    if not solve_n_queens(board, 0, n):
        print("No solution exists for the given N.")
if __name__ == "__main__":
    n_queens()
