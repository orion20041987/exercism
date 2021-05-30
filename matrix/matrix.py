class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [[int(elem) for elem in row.split()] for row in matrix_string.splitlines()]

    def row(self, index):
        return [elem for elem in self.matrix_string[index - 1]]

    def column(self, index):
        return [row[index - 1] for row in self.matrix_string]


matrix = Matrix("1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n17 18 19 20\n21 22 23 24\n25 26 27 28")

print(matrix.row(3))
print(matrix.column(3))
matrix.row(3)[0] = 999
matrix.column(3)[0] = 777
print(matrix.row(3))
print(matrix.column(3))
