import sublime
import sublime_plugin
import sys
import os

sys.path.append(os.path.dirname(__file__))
import ledger_core as core

class LedgerAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        is_transaction_header = True
        is_posting = True

        print ('XXX')

        for loc in [view.substr(view.line(x)) for x in locations]:
            print(loc)
            is_transaction_header = False if not core.is_transaction_header(loc) else is_transaction_header
            is_posting = False if not core.is_posting(loc) else is_posting

        print (is_posting)
        print (is_transaction_header)

        if is_posting == is_transaction_header:
            return None

        print ('HELLO')

        payees, accounts = core.parse(self.content(view))
        if is_transaction_header:
            return self.to_autocomplete(payees), sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS
        elif is_posting:
            for loc in [view.substr(view.line(x)) for x in locations]:
                account = core.parse_account_string(loc)
                if account is not None:
                    return self.to_autocomplete(accounts.keys()), sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS

                account = core.parse_account_string(account[:account.rfind(':')])
                while(True):
                    if accounts is None:
                        return None

                    if account.keys()[0] not in accounts.keys():
                        return self.to_autocomplete(accounts.keys()), sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS
                    else:
                        accounts = accounts[account.keys()[0]]
        else:
            assert False

    @staticmethod
    def content(view):
        return view.substr(sublime.Region(0, view.size()))

    @staticmethod
    def to_autocomplete(lst):
        return [[x, x] for x in lst]
