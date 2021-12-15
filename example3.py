#!/usr/bin/env python

from choose_receipts import choose_receipts, print_selection_result


def main():
    s = '''42257.09
426.40
274.38
143.24
140.92
1446.00
5293.80
5293.80
4263.60
516.84
414.28
84.33
200.94
470.43
246.58
40.37
161.00
212.15
317.20
254.05'''

    values = s.split('\n')
    result, exact = choose_receipts(values, ['12345.88'])
    print()
    print_selection_result(result, exact)

    # One possible exact solution is:
    # sum of all chooses = 12345.88 ✔
    # 12345.88: (426.40, 143.24, 5293.80, 5293.80, 516.84, 470.43, 40.37, 161.00)
    # remain: (42257.09, 274.38, 140.92, 1446.00, 4263.60, 414.28, 84.33, 200.94, 246.58, 212.15, 317.20, 254.05)


if __name__ == '__main__':
    main()
