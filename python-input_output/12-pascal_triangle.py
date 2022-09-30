#!/usr/bin/python3
"Creates a Pascal triangle"


def pascal_triangle(n):
    "Returns the Pascal triangle of n"
    triangle = []

    for i in range(n):
        part = []
        for j in range(i + 1):
            if i <= 1:
                part.append(1)
            else:
                if j == 0 or j == i:
                    part.append(1)
                else:
                    part.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(part)
    return triangle
