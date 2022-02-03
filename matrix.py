"""
Nick Swanson
CIS 211
Code demo
"""

from typing import List

class Vector(list):

    def __mul__(self, other):
        # Computes the dot product with another vector; return Int

        assert len(self) == len(other)

        value = 0
        for i in range(len(self)):
            value += self[i] * other[i]
        return value

    def matrix_mult(self, matrix):
        # Computes the multiplication of of the current vector by a matrix; return a resulting vector

        assert len(self) == len(matrix.rows)
        result = Vector()

        for i in matrix.cols:
            value = self * i
            result.append(value)
        return result

class Matrix:

    def __init__(self, r: List["Vector"]):
        # Receives a Vector list representing the rows of the Matrix as an argument

        self.rows = r
        self.cols = []

        for col in range(len(self.rows[0])):
            current_col = Vector()
            for row in range(len(self.rows)):
                current_col.append(self.rows[row][col])
            self.cols.append(current_col)


v = Vector([1, 2])
v2 = Vector([3, 4])
m = Matrix([v2, Vector([5, 6])])
print(v.matrix_mult(m))
