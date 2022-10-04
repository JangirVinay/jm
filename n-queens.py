N = 8
size = N

def print_matrix(matrix):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end="   |   ")
        print('--------' * size)

    print("\n")

def print_solution(board: "list[int][int]") -> None:

    for i in range(N):
        for j in range(N):
            print(board[i][j])
        print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    
    for i in range(col):
        if board[row][i]:
            return False

    i = row
    j = col

    while (i >= 0 and j >= 0):
        if (board[i][j]): return False
        i -= 1
        j -= 1

    i = row
    j = col

    while (i < N and j < N):
        if (board[i][j]): return False
        i += 1
        j += 1

    i = row
    j = col

    while (i >= 0 and j < N):
        if (board[i][j]): return False
        i -= 1
        j += 1

    i = row
    j = col

    while (i < N and j >= 0):
        if (board[i][j]): return False
        i += 1
        j -= 1

    return True

def backtrack(board, row = 0):
    if row >= N:
        return True

    for i in range(N):
        if is_safe(board, row, i):
            board[row][i] = 1

            if backtrack(board, row + 1):
                return True

            board[row][i] = 0

    return False

def n_size_matrix():
    board = []

    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(0)

        board.append(row)
    
    return board


def main():
    board = n_size_matrix()
    
    backtrack(board)

    print_matrix(board)


main()
