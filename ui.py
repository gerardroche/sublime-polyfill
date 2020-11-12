import os


from sublime import active_window
from sublime import find_resources
from sublime import load_settings
from sublime import save_settings
import sublime_plugin


def _load_preferences():
    return load_settings('Preferences.sublime-settings')


def _save_preferences():
    return save_settings('Preferences.sublime-settings')


class EnableColorSchemeCommand(sublime_plugin.ApplicationCommand):

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
            color_scheme = _load_preferences().get('color_scheme')
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

        preferences = _load_preferences()
        preferences.set('color_scheme', color_scheme)
        _save_preferences()

        for view in self.window.views():
            view.settings().erase('color_scheme')


class EnableThemeCommand(sublime_plugin.ApplicationCommand):

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

        preferences = _load_preferences()
        preferences.set('theme', theme)
        _save_preferences()


class OverlayOpenFileCommand(sublime_plugin.WindowCommand):
    """Open File; Inspired by Vim CtrlP (https://kien.github.io/ctrlp.vim)."""

    def run(self, tab=None, split=None, vsplit=None):
        """
        Open file from overlay.

        :param tab:
            Open the selected file in a new tab
        :param split:
            Open the selected file in a horizontal split
        :param vsplit:
            Open the selected file in a vertical split

        Defaults to opening in a new tab.
        """
        transient_view = self.window.transient_view_in_group(self.window.active_group())
        if not transient_view:
            return

        fname = transient_view.file_name()
        if not fname:
            return

        if vsplit:
            self.open_file_in_vertical_split(fname)
        elif split:
            self.open_file_in_horizontal_split(fname)
        elif tab:
            self.open_file_in_tab(fname)
        else:
            self.open_file_in_tab(fname)

        self.window.run_command('hide_overlay')

    def is_enabled(self):
        view = self.window.active_view()
        if view:
            return bool(view.settings().get('polyfill.experimental_features'))
        return False

    def open_file_in_vertical_split(self, fname):
        self.window.open_file(fname)
        self.window.run_command('create_pane_with_file', {'direction': 'right'})

    def open_file_in_horizontal_split(self, fname):
        self.window.open_file(fname)
        self.window.run_command('create_pane_with_file', {'direction': 'down'})

    def open_file_in_tab(self, fname):
        self.window.open_file(fname)


class PolyfillSetLayoutCommand(sublime_plugin.WindowCommand):

    def run(self, cols, rows, cells):
        num_groups_before = self.window.num_groups()
        active_group_before = self.window.active_group()

        self.window.run_command('set_layout', {
            'cols': cols,
            'rows': rows,
            'cells': cells
        })

        if num_groups_before == self.window.num_groups():
            # Fix issue where group focus moves when it probably shouldn't.
            # When the layout is not changed then the focus shouldn't change
            # either. Previously, if the active view before the layout change
            # is transient ST would move the cursor focus to a group with a
            # non-transient view. This can be disorienting and interrupt flow
            # because where the cursor focus has moved to is not always clear.
            self.window.focus_group(active_group_before)
            return

        if len(self.window.views_in_group(active_group_before)) < 2:
            # Only move the active view before layout change to the new group
            # if it doesn't leave the previous group without any views.
            return

        view = self.window.active_view_in_group(active_group_before)
        self.window.set_view_index(view, self.window.active_group(), 0)
