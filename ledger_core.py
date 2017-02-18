import re


def is_transaction_header(line):
    date = '(?P<date>[\\d\\./-]+)'
    print(re.match('^' + date + '.*', line) is not None)
    return re.match('^' + date + '.*', line) is not None


def is_posting(line):
    print(re.match('^' + ' |\\t' + '.*', line) is not None)
    return re.match('^' + ' |\\t' + '.*', line) is not None


def parse_payee(line):
    date = '(?P<date>[\\d\\./-]+)'
    mark = '([!|*] )?'
    payee = '(?P<payee>.*)'
    m = re.match('^' + date + '(' + ' ' + mark + payee + ')?', line)
    if not m:
        return None

    parsed = m.group('payee')

    return None if parsed == '' else parsed


def parse_account_string(line):
    if line == '':
        return None

    if line[0] != ' ' and line[0] != '\t':
        return None

    tokens = re.split('  +|\t', line.lstrip())
    if len(tokens) < 1:
        return None

    return tokens[0]


def to_account(line):
    parts = line.split(':')
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


def parse(journal):
    payees = set()
    accounts = {}

    for line in journal.splitlines():
        if not parse_payee(line) is None:
            payees.add(parse_payee(line))
        elif not parse_account_string(line) is None:
            accounts = merge_dict(accounts, to_account(parse_account_string(line)))

    return sorted(list(payees)), accounts

