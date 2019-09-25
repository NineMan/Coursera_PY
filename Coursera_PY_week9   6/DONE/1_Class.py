from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        answer = ''
        for i in self.matrix:
            for j in i:
                answer = answer + str(j) + '\t'
            answer = answer[:-1] + '\n'
        return answer[:-1]

    def size(self):
        len_col = len(self.matrix)
        len_str = len(self.matrix[0])
        return (len_col, len_str)


exec(stdin.read())
