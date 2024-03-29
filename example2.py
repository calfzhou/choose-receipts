#!/usr/bin/env python

from choose_receipts import choose_receipts, print_selection_result


def main():
    s = '''61.19
70.81
59.92
107.97
540.21
43.04
99.79
126.06
147.52
77.56
92.29
47.64
118.46
47.32
72.71
70.84
59.87
118.71
25.33
25.46
3431.21
25.42
7.74
204.34
48.94
0.03
309.71
375.58
1016.14
870.48
16.48
2749.14
1695.8
184.37'''

    values = s.split('\n')
    result, exact = choose_receipts(values, ['8403.61'])
    print()
    print_selection_result(result, exact)

    # One possible exact solution is:
    # sum of all chooses = 8403.61 ✔
    # 8403.61: (61.19, 77.56, 3431.21, 204.34, 2749.14, 1695.8, 184.37)
    # remain: (70.81, 59.92, 107.97, 540.21, 43.04, 99.79, 126.06, 147.52, 92.29, 47.64, 118.46, 47.32, 72.71, 70.84, 59.87, 118.71, 25.33, 25.46, 25.42, 7.74, 48.94, 0.03, 309.71, 375.58, 1016.14, 870.48, 16.48)


if __name__ == '__main__':
    main()
