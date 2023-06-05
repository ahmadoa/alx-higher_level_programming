#!/usr/bin/python3
"""nqueens problem is solved using the backtracking algorithm in order
for the queens to be positioned ina non-attacking spots
"""


from sys import argv

if __name__ == "__main__":
    solution = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # solution list
    for i in range(n):
        solution.append([i, None])

    def exists(y):
        """function that checks if a queen exits in a vertical cell"""
        for x in range(n):
            if y == solution[x][1]:
                return True
        return False

    def decline(x, y):
        """decline or accept a solution"""
        if (exists(y)):
            return False
        index = 0
        while index < x:
            if abs(a[index][1] - y) == abs(index - x):
                return False
            index += 1
        return True

    def clear_solution(x):
        """ckears the failed solution"""
        for i in range(x, n):
            solution[i][1] = None

    def nqueens(x):
        """backtracking to find solution"""
        for y in range(n):
            clear_solution(x)
            if decline(x, y):
                solution[x][1] = y
                if (x == n - 1):
                    print(solution)
                else:
                    nqueens(x + 1)
    nqueen(0)
