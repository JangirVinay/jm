size = int(input('enter size:'))

def init_matrix(matrix):
    for _ in range(size):
        row = []
        for __ in range(size):
            row.append(0)

        matrix.append(row)

    return matrix

def set_value(matrix, value, pos):
    x, y = pos[0], pos[1]
    matrix[x][y] = value

def print_matrix(matrix):
    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end="   |   ")
        print('--------' * size)

    print("\n")

def magic_sqaure():
    counter = 1

    curr_pos_x = 0
    curr_pos_y = int(size/2)

    matrix = init_matrix([]) # [[0, 0, 0],
    #[0, 1, 0],
    #[0, 0, 0],
    #[0, 0, 2]] 

    print('insert: 1')
    set_value(matrix, counter, [curr_pos_x, curr_pos_y])

    print_matrix(matrix)

    while counter != size * size:

        # up instruction
        x = (curr_pos_x - 1) % size # -1 because we move up

        # right instruction
        y = (curr_pos_y + 1) % size # +1 because we move ahead

        counter += 1

        if (matrix[x][y] == 0):
            curr_pos_x = x
            curr_pos_y = y

            set_value(matrix, counter, [x, y])
        else:
            x = (curr_pos_x + 1) % size
            curr_pos_x = x
            set_value(matrix, counter, [x, curr_pos_y])
        
        print('insert:', counter)
        print_matrix(matrix)


magic_sqaure()
