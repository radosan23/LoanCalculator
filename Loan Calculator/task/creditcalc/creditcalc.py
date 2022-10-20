import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type')
parser.add_argument('-a', '--payment')
parser.add_argument('-p', '--principal')
parser.add_argument('-n', '--periods')
parser.add_argument('-i', '--interest')
args = parser.parse_args()
t = args.type if args.type is not None else ''
p = int(args.principal) if args.principal is not None else 0
a = int(args.payment) if args.payment is not None else 0
n = int(args.periods) if args.periods is not None else 0
i = float(args.interest) / 100 / 12 if args.interest is not None else -1

if t == 'diff' and p > 0 and a == 0 and n > 0 and i >= 0:
    overpay = 0
    for m in range(1, n+1):
        d = math.ceil(p / n + (i * (p - p * (m - 1) / n)))
        overpay += d
        print(f'Month {m}: payment is {d}')
    print(f'\nOverpayment = {overpay - p}')
elif t == 'annuity' and p > 0 and a > 0 and n == 0 and i >= 0:
    n = math.ceil(math.log((a / (a - i * p)), 1 + i))
    overpay = math.ceil(a * n - p)
    if n < 12:
        print(f'It will take {n} month{"" if n == 1 else "s"} to repay this loan!')
    elif n % 12 == 0:
        print(f'It will take {n // 12} year{"" if n / 12 == 1 else "s"} to repay this loan!')
    else:
        print(f'It will take {n // 12} year{"" if n // 12 == 1 else "s"} '
              f'and {n % 12} month{"" if n % 12 == 1 else "s"} to repay this loan!')
    print(f'Overpayment = {overpay}')
elif t == 'annuity' and p > 0 and a == 0 and n > 0 and i >= 0:
    a = math.ceil(p * (i * pow(1 + i, n) / (pow(1 + i, n) - 1)))
    overpay = a * n - p
    print(f'Your annuity payment = {a}!')
    print(f'Overpayment = {overpay}')
elif t == 'annuity' and p == 0 and a > 0 and n > 0 and i >= 0:
    p = int(a / (i * pow(1 + i, n) / (pow(1 + i, n) - 1)))
    overpay = a * n - p
    print(f'Your loan principal = {p}!')
    print(f'Overpayment = {overpay}')
else:
    print('Incorrect parameters.')
