import os


import sublime
import sublime_plugin


class EnableThemeCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        self.themes = []

        for theme in sublime.find_resources('*.sublime-theme'):
            if "Addon" not in theme and "tests" not in theme:
                self.themes.append(os.path.basename(theme))

        if len(self.themes) > 1:
            sublime.active_window().show_quick_panel(self.themes, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        theme = self.themes[index]

        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('theme', theme)
        sublime.save_settings('Preferences.sublime-settings')


class EnableColorSchemeCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        self.color_schemes = []

        for color_scheme in sublime.find_resources('*.tmTheme'):
            if "(SL)" not in color_scheme and "tests" not in color_scheme:
                self.color_schemes.append(color_scheme)

        if len(self.color_schemes) > 1:
            color_scheme = sublime.load_settings('Preferences.sublime-settings').get('color_scheme')
            if color_scheme not in self.color_schemes:
                self.color_schemes.insert(0, color_scheme)

            self.window = sublime.active_window()
            self.window.show_quick_panel(
                self.color_schemes,
                self.on_done,
                0,
                self.color_schemes.index(color_scheme),
                self.on_select
            )

    def on_select(self, index):
        if index == -1:
            return

        color_scheme = self.color_schemes[index]

        for group in range(0, self.window.num_groups()):
            active_view_in_group = self.window.active_view_in_group(group)
            if active_view_in_group:
                active_view_in_group.settings().set('color_scheme', color_scheme)

    def on_done(self, index):
        if index == -1:
            for view in self.window.views():
                view.settings().erase('color_scheme')
            return

        color_scheme = self.color_schemes[index]

        settings = sublime.load_settings('Preferences.sublime-settings')
        settings.set('color_scheme', color_scheme)
        sublime.save_settings('Preferences.sublime-settings')

        for view in self.window.views():
            view.settings().erase('color_scheme')
