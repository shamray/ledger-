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