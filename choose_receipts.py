#!/usr/bin/env python

import argparse
from decimal import Decimal
import itertools


def to_decimal(val):
    if isinstance(val, (Decimal, int)):
        return val
    elif isinstance(val, str):
        return Decimal(val)
    elif isinstance(val, float):
        return Decimal('%f' % val)
    else:
        return Decimal(val)


def choose_receipts(values, targets):
    values = list(map(to_decimal, values))
    targets = list(map(to_decimal, targets))
    total = sum(values)
    target = sum(targets)
    print(f'total: {total} vs target: {target} [{", ".join(str(x) for x in targets)}]')
    if total < target:
        return None

    min_sum = total + 1
    min_selections = None
    indexes = range(len(values))
    desc_values = list(reversed(sorted(values)))

    for cnt in range(len(targets), len(values) + 1):
        if sum(desc_values[:cnt]) < target:
            continue

        print(f'try using {cnt} receipts')
        for selection in itertools.combinations(indexes, cnt):
            s = sum(values[i] for i in selection)
            if s < target or s >= min_sum:
                continue

            splits = _find_possible_splits(values, selection, targets)
            if splits:
                min_sum = s
                min_selections = _apply_splits(values, splits)
                print(min_sum, ', '.join(f'({", ".join(str(x) for x in sel)})' for sel in min_selections))
                if min_sum == target:
                    return min_selections, True

    return min_selections, False


def print_selection_result(selection_plan, exact=False):
    target_satisfies = list(sum(values) for values in selection_plan[:-1])
    total_satisfy = sum(target_satisfies)
    print(f"sum of all chooses = {total_satisfy} {'✔' if exact else '×'}")
    for i, values in enumerate(selection_plan[:-1]):
        print(f'{target_satisfies[i]}: ({", ".join(str(x) for x in values)})')

    print(f'remain: ({", ".join(str(x) for x in selection_plan[-1])})')



def _find_possible_splits(values, indexes, targets):
    splits = _split_one_by_one(values, indexes, targets)
    return splits


def _split_one_by_one(values, indexes, targets):
    if len(targets) == 1:
        return [indexes]

    total = sum(values[i] for i in indexes)
    target = sum(targets)
    desc_values = list(reversed(sorted(values[i] for i in indexes)))

    for cnt in range(1, len(indexes) - len(targets) + 2):
        if sum(desc_values[:cnt]) < targets[0] or total - sum(desc_values[-cnt:]) < target - targets[0]:
            continue

        for selection in itertools.combinations(indexes, cnt):
            s = sum(values[i] for i in selection)
            if s >= targets[0] and total - s >= target - targets[0]:
                res = _split_one_by_one(values, _array_sub(indexes, selection), targets[1:])
                if res:
                    splits = [selection]
                    splits.extend(res)
                    return splits

    return None


def _apply_splits(values, splits):
    parts = [tuple(values[i] for i in group) for group in splits]
    indexes = range(len(values))
    for group in splits:
        indexes = _array_sub(indexes, group)

    remain = [values[i] for i in indexes]
    parts.append(remain)
    return parts


def _array_sub(source, to_remove):
    return [i for i in source if i not in to_remove]


def main():
    parser = argparse.ArgumentParser(description='Receipts Chooser')
    parser.add_argument('-t', '--targets', type=Decimal, nargs='+', metavar='TARGET', required=True,
                        help='the target number(s)')
    parser.add_argument('-v', '--values', type=Decimal, nargs='+', metavar='VALUE', required=True,
                        help='the raw receipt value(s)')

    args = parser.parse_args()
    choose_receipts(args.values, args.targets)


if __name__ == '__main__':
    main()
