import sublime
import sublime_plugin


class TryExampleCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sublime.error_message("Try example\n")
        return None
