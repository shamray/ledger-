import re

def parse_payee(str):
    date = '(?P<date>[\\d\\./-]+)'
    mark = '([!|*] )?'
    payee = '(?P<payee>.*)'
    m = re.match('^' + date + ' ' + mark + payee, str)
    if not m:
        return ''

    return m.group('payee')

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