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

    def test_transaction_without_payee_space(self):
        self.assertEqual(parse_payee('2015/10/16 '), '')

    def test_transaction_without_payee(self):
        self.assertEqual(parse_payee('2015/10/16'), '')

    def test_transaction_wrong_string(self):
        self.assertEqual(parse_payee(' expenses:food  $10'), None)


class ParseAccountString(unittest.TestCase):
    def test_account_with_amount(self):
        self.assertEqual(parse_account_string(' expenses:food  $10'), 'expenses:food')

    def test_account_without_amount(self):
        self.assertEqual(parse_account_string(' expenses:food'), 'expenses:food')

    def test_account_wide_indent(self):
        self.assertEqual(parse_account_string('    expenses:food  $10'), 'expenses:food')

    def test_account_wide_spacing(self):
        self.assertEqual(parse_account_string(' expenses:food    $10'), 'expenses:food')

if __name__ == '__main__':
    unittest.main()