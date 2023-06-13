#!/usr/bin/python3

matrix_mul = __import__('100-matrix_mul').matrix_mul

mat0 = [[2.5, 3.1], [2.2, 2.7]]
mat1 = [[1, 2], [3, 4]]
mat2 = [[1, 3, 2], [2, 1, 3]]
mat3 = []
mat4 = [[]]
mat5 = [[1, 2, 3], [2, 2]]
mat6 = [[1, 2, '66'], [2+8j, 2, {}]]
mat7 = ['stringify', [2, 2, 4]]
mat8 = 'Odogwu'


print(matrix_mul(mat1, mat2, mat3))
