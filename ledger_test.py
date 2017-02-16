import unittest
from ledger_core import *


class Parse(unittest.TestCase):
    def test_one_transaction(self):
        journal = '2015/10/16 bought food\n expenses:food  $10\n assets:cash'
        transactions = ['bought food']
        accounts = {
            'expenses': {
                'food': {}
            },
            'assets': {
                'cash': {}
            }
        }
        self.assertEqual(parse(journal), (transactions, accounts))


class ParsePayee(unittest.TestCase):
    def test_transaction_with_payee(self):
        self.assertEqual(parse_payee('2015/10/16 bought food'), 'bought food')


if __name__ == '__main__':
    unittest.main()