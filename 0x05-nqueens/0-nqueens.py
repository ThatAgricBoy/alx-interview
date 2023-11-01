#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n, board, col):
    if col == n:
        solutions.append(board[:])
        return
    for row in range(n):
        if all(is_safe(board[i], row, col, n) for i in range(col)):
            board[col] = row
            solve_nqueens(n, board, col + 1)

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print([i, row] for i in range(len(solution)))
        print()

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        
        solutions = []
        board = [-1] * n
        solve_nqueens(n, board, 0)
        print_solutions(solutions)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
