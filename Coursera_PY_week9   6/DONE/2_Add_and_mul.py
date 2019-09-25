from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        # self.matrix = deepcopy(matrix)
        self.matrix = matrix

    def __str__(self):
        answer = ''
        for i in self.matrix:
            for j in i:
                answer = answer + str(j) + '\t'
            answer = answer[:-1] + '\n'
        return answer[:-1]

    def __add__(self, other):
        matr = deepcopy(self.matrix)
        for i in range(len(matr)):
            for j in range(len(matr[i])):
                matr[i][j] = matr[i][j] + other.matrix[i][j]
        return Matrix(matr)

    def __mul__(self, other):
        matr = deepcopy(self.matrix)
        if isinstance(other, int) or isinstance(other, float):
            for i in range(len(matr)):
                for j in range(len(matr[i])):
                    matr[i][j] = matr[i][j] * other
        return Matrix(matr)

    __rmul__ = __mul__

    def size(self):
        len_col = len(self.matrix)
        len_str = len(self.matrix[0])
        return (len_col, len_str)


# m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# alpha = 15
# print(m1)
# print()
# print(m2)
# print()
print(m1 + m2)
# print(m * alpha)
# print(alpha * m)
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m.size())
exec(stdin.read())
