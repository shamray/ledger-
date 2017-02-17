import re


def parse_payee(str):
    date = '(?P<date>[\\d\\./-]+)'
    mark = '([!|*] )?'
    payee = '(?P<payee>.*)'
    m = re.match('^' + date + '(' + ' ' + mark + payee + ')?', str)
    if not m:
        return None

    parsed = m.group('payee')

    return '' if parsed is None else parsed


def parse_account_string(str):
    if str[0] != ' ' and str[0] != '\t':
        return None

    tokens = re.split('  +|\t', str.lstrip())
    if len(tokens) < 1:
        return None

    return tokens[0]

def to_account(str):
    parts = str.split(':')
    acc = None

    for part in reversed(parts):
        acc = {part: acc}

    return acc


def merge_dict(left, right):
    assert(isinstance(left, dict) or left is None)
    assert(isinstance(right, dict) or right is None)

    if left is None:
        return right
    elif right is None:
        return left

    for key, value in right.items():
        if key not in left:
            left[key] = value
        else:
            left[key] = merge_dict(left[key], value)

    return left


def parse(jorunal):
    return (
    ['bought food'],
    {
        'expenses':
        {
            'food': {}
        },
        'assets': {
            'cash': {}
        }
    }
)