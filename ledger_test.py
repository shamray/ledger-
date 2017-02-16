import unittest
from ledger_core import *


class Parse(unittest.TestCase):
    def one_transaction(self):
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


if __name__ == '__main__':
    unittest.main()