#!/usr/bin/env python3

def determinant(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if len(matrix) == 1:
        return matrix[0][0]
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum(((-1) ** c) * matrix[0][c] * determinant([row[:c] + row[c+1:] for row in matrix[1:]]) for c in range(len(matrix)))
