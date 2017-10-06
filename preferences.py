import os

from sublime import active_window
from sublime import find_resources
from sublime import load_settings
from sublime import save_settings
from sublime_plugin import ApplicationCommand


class EnableThemeCommand(ApplicationCommand):

    def run(self):
        self.themes = []

        for theme in find_resources('*.sublime-theme'):
            ignore = False
            for exclude in ['Addon', 'tests']:
                if exclude in theme:
                    ignore = True

            if not ignore:
                self.themes.append(os.path.basename(theme))

        if len(self.themes) > 1:
            active_window().show_quick_panel(self.themes, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        theme = self.themes[index]

        settings = load_settings('Preferences.sublime-settings')
        settings.set('theme', theme)
        save_settings('Preferences.sublime-settings')


class EnableColorSchemeCommand(ApplicationCommand):

    def run(self):
        self.color_schemes = []

        for color_scheme in find_resources('*.tmTheme'):
            ignore = False
            for exclude in ['(SL)', 'Color Highlighter', 'tests']:
                if exclude in color_scheme:
                    ignore = True

            if not ignore:
                self.color_schemes.append(color_scheme)

        if len(self.color_schemes) > 1:
            color_scheme = load_settings('Preferences.sublime-settings').get('color_scheme')
            if color_scheme not in self.color_schemes:
                self.color_schemes.insert(0, color_scheme)

            self.window = active_window()
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

        settings = load_settings('Preferences.sublime-settings')
        settings.set('color_scheme', color_scheme)
        save_settings('Preferences.sublime-settings')

        for view in self.window.views():
            view.settings().erase('color_scheme')
