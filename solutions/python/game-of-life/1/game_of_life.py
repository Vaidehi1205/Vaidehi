def tick(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0

            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    if (x, y) != (i, j):
                        live_neighbors += matrix[x][y]

            if matrix[i][j] == 1:
                if live_neighbors in (2, 3):
                    result[i][j] = 1
            elif live_neighbors == 3:
                result[i][j] = 1

    return result