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

    def test_account_with_spaces_with_amount(self):
        self.assertEqual(parse_account_string(' expenses:fast food  $10'), 'expenses:fast food')

    def test_account_with_spaces_with_amount(self):
        self.assertEqual(parse_account_string(' expenses:fast food'), 'expenses:fast food')

class ToAccount(unittest.TestCase):
    def test_1_level(self):
        self.assertEqual(to_account('expenses'), {'expenses': None})

    def test_2_levels(self):
        self.assertEqual(to_account('expenses:food'), {'expenses': {'food': None}})

class MergeDict(unittest.TestCase):
    def test_1_level_no_intersection(self):
        left = {'apples': None}
        right = {'oranges': None}

        self.assertEqual(merge_dict(left, right), {'apples': None, 'oranges': None})

    def test_2_levels_1_level(self):
        left = {'fruits': {'apples': None, 'oranges': None}}
        right = {'veggies': None}

        self.assertEqual(merge_dict(left, right), {'fruits': {'apples': None, 'oranges': None}, 'veggies': None})

    def test_1_levels_2_levels(self):
        left = {'veggies': None}
        right = {'fruits': {'apples': None, 'oranges': None}}

        self.assertEqual(merge_dict(left, right), {'fruits': {'apples': None, 'oranges': None}, 'veggies': None})


if __name__ == '__main__':
    unittest.main()