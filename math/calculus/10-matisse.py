#!/usr/bin/env python3
def poly_derivative(poly):
    if type(poly) is not list or len(poly) == 0:
        return None

    for coefficient in poly:
        if type(coefficient) not in [int, float]:
            return None

    if len(poly) == 1:
        return [0]

    derivative = [i * poly[i] for i in range(1, len(poly))]

    if derivative == []:
        return [0]

    return derivative
