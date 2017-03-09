import sublime
import sublime_plugin
import sys
import os

sys.path.append(os.path.dirname(__file__))
import ledger_core as core


class LedgerAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        location_strings = [view.substr(view.line(x)) for x in locations]
        content_string = self.content(view)

        try:
            location = view.sel()[0].begin()
            print (view.match_selector(location, 'source.ledger'))
        except IndexError:
            print('???')

        r = core.suggest_completion(content_string, location_strings)
        ac = self.to_autocomplete(r)
        if ac is None:
            return []
        else:
            return ac, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS

    @staticmethod
    def content(view):
        return view.substr(sublime.Region(0, view.size()))

    @staticmethod
    def to_autocomplete(lst):
        if lst is None:
            return None

        return [[x, x] for x in lst]
