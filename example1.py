#!/usr/bin/env python

from choose_receipts import choose_receipts, print_selection_result


def main():
    s = '''210
    267
    138
    233
    194
    164
    525
    430
    497
    500
    300
    427
    344
    153
    600
    349
    237
    243
    390
    250
    340
    712
    1000
    245
    787
    376
    39
    29
    38
    39
    38
    76
    27
    27'''

    values = [int(v) for v in s.split('\n')]
    result, exact = choose_receipts(values, [850, 4700, 4300])
    print()
    print_selection_result(result, exact)

    # One possible exact solution is:
    # sum of all chooses = 9850 ✔
    # 850: (138, 712)
    # 4700: (210, 525, 497, 500, 344, 600, 237, 1000, 787)
    # 4300: (267, 233, 194, 430, 300, 427, 153, 349, 243, 390, 250, 340, 245, 376, 76, 27)
    # remain: (164, 39, 29, 38, 39, 38, 27)


if __name__ == '__main__':
    main()
