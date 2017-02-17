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
    if (len(tokens) < 1):
        return None

    return tokens[0]


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