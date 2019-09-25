from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        lenghtSelf = Matrix(self.matrix).size()
        lenghtOther = Matrix(other.matrix).size()
        matr1 = deepcopy(self.matrix)
        if(lenghtSelf == lenghtOther):
            for i in range(len(matr1)):
                for j in range(len(matr1[i])):
                    matr1[i][j] = matr1[i][j] + other.matrix[i][j]
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(matr1)

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

    def transpose(self):
        temp = list(zip(*self.matrix))
        tmatrix = []
        for i in temp:
            tmatrix.append(list(i))
        self.matrix = tmatrix
        return Matrix(tmatrix)

    # @staticmethod
    def transposed(self):
        temp = list(zip(*self.matrix))
        tmatrix = []
        for i in temp:
            tmatrix.append(list(i))
        return Matrix(tmatrix)


# Task 3 check 1
# Check exception to add method
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)
#
# m2 = Matrix([[0, 1, 0], [20, 0, -1]])
# try:
#     m = m1 + m2
#     print('WA\n' + str(m))
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)
#
# Task 3 check 2
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m)
# m1 = m.transpose()
# print(m)
# print(m1)
#
# Task 3 check 3
# m = Matrix([[10, 10], [0, 0], [1, 1]])
# print(m)
# print(Matrix.transposed(m))
# print(m)

# Task 4 check 4
# m1 = Matrix([[1, 0, 0], [0, 1, 0]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1]])
# print(Matrix.transposed(m1) + Matrix.transposed(m2))
# try:
#     t = Matrix.transposed(m1) + m2
#     print('WA it should be exception')
# except MatrixError as e:
#     print(e.matrix1)
#     print(e.matrix2)
exec(stdin.read())
