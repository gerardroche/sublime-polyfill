import json
import os


from sublime import active_window
from sublime import find_resources
from sublime import load_settings
from sublime import packages_path
from sublime import save_settings
from sublime import status_message
import sublime_plugin


def _load_preferences():
    return load_settings('Preferences.sublime-settings')


def _save_preferences():
    return save_settings('Preferences.sublime-settings')


class ClearWindowCommand(sublime_plugin.WindowCommand):

    def run(self):
        if self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(False)

        if self.window.is_minimap_visible():
            self.window.set_minimap_visible(False)

        if self.window.is_menu_visible():
            self.window.set_menu_visible(False)

        if self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(False)

        self.window.run_command('resize_groups_almost_equally')

        preferences = _load_preferences()
        preferences.set('indent_guide_options', [])
        preferences.set('line_numbers', False)
        preferences.set('draw_white_space', 'selection')
        preferences.set('rulers', [])
        _save_preferences()

        self.window.run_command('sort_user_settings')


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


class PromptOpenRecentProjectCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.recent_workspaces = self.get_recent_workspaces()
        if not self.recent_workspaces:
            return False

        # only display workspaces that really exist
        self.recent_workspaces_that_really_exist = []
        for recent_workspace in self.recent_workspaces:
            if os.path.isfile(os.path.expanduser(recent_workspace)):
                self.recent_workspaces_that_really_exist.append(recent_workspace)

        self.window.show_quick_panel(self.recent_workspaces_that_really_exist, self.on_done)

    def on_done(self, index):
        if index == -1:
            return

        picked = self.recent_workspaces_that_really_exist[index]
        index = self.recent_workspaces.index(picked)

        self.window.run_command('open_recent_project_or_workspace', {'index': index})

    def get_recent_workspaces(self):
        """Return list > 0; otherwise None."""
        session = self.load_session()
        if not session:
            return None

        workspaces = session.get('workspaces')
        if not workspaces:
            return None

        recent_workspaces = workspaces.get('recent_workspaces')
        if not recent_workspaces:
            return None

        # substitute user home dir with ~
        user_home_dir = os.getenv('HOME')
        recent_workspaces_list = []
        for recent_workspace in recent_workspaces:
            if recent_workspace.startswith(user_home_dir):
                recent_workspaces_list.append(recent_workspace.replace(user_home_dir, '~'))
            else:
                recent_workspaces_list.append(recent_workspace)

        if recent_workspaces_list and len(recent_workspaces_list) > 0:
            return recent_workspaces_list

        return None

    def load_session(self):
        """Return dict or None if no session exists."""
        local_session_path = os.path.join(os.path.dirname(packages_path()), 'Local')
        local_auto_save_session_file = os.path.join(local_session_path, 'Auto Save Session.sublime_session')
        local_session_file = os.path.join(local_session_path, 'Session.sublime_session')

        if os.path.isfile(local_auto_save_session_file):
            session_file_to_use = local_auto_save_session_file
        elif os.path.isfile(local_session_file):
            session_file_to_use = local_session_file
        else:
            return None

        with open(session_file_to_use) as f:
            local_session_content = f.read()

        session = json.loads(local_session_content, strict=False)

        return session


class ResetWindowCommand(sublime_plugin.WindowCommand):

    def run(self):

        self.window.run_command('reset_font_size')

        if not self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(True)

        if not self.window.is_minimap_visible():
            self.window.set_minimap_visible(True)

        if not self.window.is_menu_visible():
            self.window.set_menu_visible(True)

        if not self.window.is_status_bar_visible():
            self.window.set_status_bar_visible(True)

        self.window.run_command('resize_groups_almost_equally')


class ResizeGroupsAlmostEquallyCommand(sublime_plugin.WindowCommand):
    """
    Resize groups equally.

    Make all groups (almost) equally high and wide, but use 'winheight' and
    'winwidth' for the current window.  Windows with 'winfixheight' set keep
    their height and windows with 'winfixwidth' set keep their width.
    @xxx winheight option
    @xxx winwidth option
    @xxx winfixheight option
    @xxx winfixwidth option
    """

    def run(self):
        layout = self.window.layout()
        col_count = len(layout['cols'])
        row_count = len(layout['rows'])

        def equalise(count):
            size = round(1.0 / (count - 1), 2)
            vals = [0.0]
            for i in range(1, count - 1):
                vals.append(round(size * i, 2))
            vals.append(1.0)
            return vals

        if col_count > 2:
            layout['cols'] = equalise(col_count)

        if row_count > 2:
            layout['rows'] = equalise(row_count)

        if col_count > 2 or row_count > 2:
            self.window.set_layout(layout)


class SortUserSettingsCommand(sublime_plugin.WindowCommand):

    def run(self):
        preferences = _load_preferences()

        # added_words
        added_words = preferences.get('added_words', [])
        added_words = list(set(added_words))
        added_words.sort()
        preferences.set('added_words', added_words)

        # ignored_packages
        ignored_packages = preferences.get('ignored_packages', [])
        ignored_packages = list(set(ignored_packages))
        ignored_packages.sort()
        preferences.set('ignored_packages', ignored_packages)

        # ignored_words
        ignored_words = preferences.get('ignored_words', [])
        ignored_words = list(set(ignored_words))
        ignored_words.sort()
        preferences.set('ignored_words', ignored_words)

        # index_exclude_patterns
        index_exclude_patterns = preferences.get('index_exclude_patterns', [])
        index_exclude_patterns = list(set(index_exclude_patterns))
        index_exclude_patterns.sort()
        preferences.set('index_exclude_patterns', index_exclude_patterns)

        # file_exclude_patterns
        file_exclude_patterns = preferences.get('file_exclude_patterns', [])
        file_exclude_patterns = list(set(file_exclude_patterns))
        file_exclude_patterns.sort()
        preferences.set('file_exclude_patterns', file_exclude_patterns)

        # folder_exclude_patterns
        folder_exclude_patterns = preferences.get('folder_exclude_patterns', [])
        folder_exclude_patterns = list(set(folder_exclude_patterns))
        folder_exclude_patterns.sort()
        preferences.set('folder_exclude_patterns', folder_exclude_patterns)

        _save_preferences()


class ToggleCommand(sublime_plugin.WindowCommand):

    def run(self):
        preferences = _load_preferences()
        preference_name = self.get_preference_name()

        if preferences.get(preference_name) != self.get_enabled_value():
            setting_value = self.get_enabled_value()
        else:
            setting_value = self.get_disable_value()

        preferences.set(preference_name, setting_value)

        _save_preferences()

        status_message('{} is {}'.format(
            self.get_preference_description(),
            'enabled' if setting_value == self.get_enabled_value() else 'disabled'
        ))

    def description(self):
        view = self.window.active_view()
        if view:
            current_value = view.settings().get(self.get_preference_name())
            if current_value == self.get_disable_value():
                return 'Show ' + self.get_preference_description()
            if current_value == self.get_enabled_value():
                return 'Hide ' + self.get_preference_description()

        return 'Toggle ' + self.get_preference_description()

    def get_preference_name(self):
        return self.name()[7:]

    def get_preference_description(self):
        return self.get_preference_name().replace('_', ' ').title()

    def get_disable_value(self):
        return False

    def get_enabled_value(self):
        return True


class ToggleFoldButtonsCommand(ToggleCommand):
    pass


class ToggleHighlightLineCommand(ToggleCommand):
    pass


class ToggleIndentGuideCommand(ToggleCommand):

    def get_preference_name(self):
        return 'indent_guide_options'

    def get_preference_description(self):
        return 'Indent Guide'

    def get_disable_value(self):
        return []

    def get_enabled_value(self):
        return ['draw_normal', 'draw_active']


class ToggleInvisiblesCommand(ToggleCommand):

    def get_preference_name(self):
        return 'draw_white_space'

    def get_disable_value(self):
        return 'selection'

    def get_enabled_value(self):
        return 'all'


class ToggleLineNumbersCommand(ToggleCommand):
    pass


class TogglePreviewOnClickCommand(ToggleCommand):

    def get_preference_description(self):
        return 'Preview on Click'


class ToggleRulersCommand(ToggleCommand):

    def get_disable_value(self):
        return []

    def get_enabled_value(self):
        return [80, 120]


class ToggleSaveOnFocusLostCommand(ToggleCommand):
    pass


class ToggleUserSettingCommand(sublime_plugin.ApplicationCommand):

    def run(self, key):
        preferences = _load_preferences()
        preferences = preferences.set(key, not bool(preferences.get(key, False)))
        _save_preferences()


class TreeView():

    def wibble_wobble(self):
        # Workaround ST API
        # * Helps scroll active file into view
        # * Helps shakes off previous sidebar (highlighted) cursor position
        self.window.run_command('move', {'by': 'lines', 'forward': True})
        self.window.run_command('move', {'by': 'lines', 'forward': False})

    def ensure_file_under_cursor_is_open(self):
        preferences = _load_preferences()
        self.preview_on_click = preferences.get('preview_on_click')

        if not self.preview_on_click:
            preferences.set('preview_on_click', True)
            _save_preferences()

        self.wibble_wobble()

    def ensure_file_under_cursor_is_open_cleanup(self):
        if not self.preview_on_click:
            preferences = _load_preferences()
            preferences.set('preview_on_click', False)
            _save_preferences()
            view = self.window.active_view()
            if view and view.is_read_only():
                view.close()

    def run_command_for_file_under_cursor(self, command):
        # There is no api to get a name of a file under the cursor in the
        # sidebar.
        #
        # The only workaround I know so far, and it's fragile at best, is
        # using the fact that the "preview_on_click" feature opens the file
        # under the cursor in a preview view. From here the file name can
        # be discovered.
        #
        # If "preview_on_click" is disabled then it needs to be temporarily
        # enabled and a "wibble wobble" workaround is used to trigger the
        # preview_on_click feature.
        #
        # The preview file seems to be marked as readonly. So, after a
        # file command is run, if the active file is readonly then it is
        # assumed to be a preview and it is closed.
        #
        # **Known Issues**
        #
        # Doesn't work if the file under cursor is a folder so don't do that.
        self.ensure_file_under_cursor_is_open()
        self.window.run_command(command)
        self.ensure_file_under_cursor_is_open_cleanup()

    def experimental_features_enabled(self):
        view = self.window.active_view()
        if view:
            return bool(view.settings().get('polyfill.experimental_features'))
        return False


class TreeViewAddFileCommand(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.run_command_for_file_under_cursor('side_bar_new_file')

    def is_enabled(self):
        return self.experimental_features_enabled()


class TreeViewAddFolderCommand(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.run_command_for_file_under_cursor('side_bar_new_directory')

    def is_enabled(self):
        return self.experimental_features_enabled()


class TreeViewDuplicateCommand(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.run_command_for_file_under_cursor('side_bar_duplicate')

    def is_enabled(self):
        return self.experimental_features_enabled()


class TreeViewFinder(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        # TODO can the current file directory be prefilled? #3
        self.window.run_command('show_panel', {'panel': 'find_in_files'})

    def is_enabled(self):
        return self.experimental_features_enabled()


class TreeViewGoToParentNode(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move_to', {'to': 'bol', 'extend': False})


class TreeViewGoToRootNode(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move', {'by': 'characters', 'forward': False})


class TreeViewGoToChildNode(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move_to', {'to': 'eol', 'extend': False})


class TreeViewMoveCommand(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.run_command_for_file_under_cursor('side_bar_rename')

    def is_enabled(self):
        return self.experimental_features_enabled()


class TreeViewMoveDown(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move', {'by': 'lines', 'forward': True})


class TreeViewMoveLeft(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move', {'by': 'characters', 'forward': False})


class TreeViewMoveRight(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move', {'by': 'characters', 'forward': True})


class TreeViewMoveUp(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        self.window.run_command('move', {'by': 'lines', 'forward': False})


class TreeViewOpenFileCommand(TreeView, sublime_plugin.WindowCommand):
    """Inspired by Vim CtrlP (https://kien.github.io/ctrlp.vim)."""

    def run(self, tab=None, split=None, vsplit=None):
        """
        Open file.

        :param tab:
            Open the selected file in a new tab
        :param split:
            Open the selected file in a horizontal split
        :param vsplit:
            Open the selected file in a vertical split

        Defaults to opening in a new tab.
        """
        # @todo open tree view file in tab #1
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

    def is_enabled(self):
        return self.experimental_features_enabled()

    def open_file_in_vertical_split(self, fname):
        self.window.open_file(fname)
        self.window.run_command('create_pane_with_file', {'direction': 'right'})

    def open_file_in_horizontal_split(self, fname):
        self.window.open_file(fname)
        self.window.run_command('create_pane_with_file', {'direction': 'down'})

    def open_file_in_tab(self, fname):
        self.window.open_file(fname)


class TreeViewRevealActiveFile(TreeView, sublime_plugin.WindowCommand):

    def run(self):
        # Try to workaround ST issues:
        # * should scroll into view if active file is not visible
        # * should focus on sidebar
        # * should highlight active file position
        # * should remove any visual artifacts from previous position
        # * navigation after reveal should begin from active file
        self.window.run_command('reveal_in_side_bar')
        self.wibble_wobble()
        self.window.run_command('focus_side_bar')


class TreeViewToggleCommand(TreeView, sublime_plugin.WindowCommand):

    def run(self, sidebar_currently_focused):
        """
        Toggle side bar.

        :param sidebar_currently_focused:
            Flag to indicate if the sidebar is currently focused
        """
        self.window.run_command('toggle_side_bar')

        if sidebar_currently_focused:
            # Ensure focus returns to active view or transient view in group
            self.window.focus_group(self.window.active_group())

            # Fix issue using Vintageous where focus changes to insert mode
            view = self.window.active_view()
            if view:
                view.run_command('_enter_normal_mode')

        else:
            # _Note_: "focus_sidebar_bar" command won't actually do anything
            # if the sidebar is not actually currently focused. Also, focus
            # is always returned to the view after the "focus_side_bar"
            # command.

            self.window.run_command('focus_side_bar')

            # If active file is off-screen then try to scroll it into view and
            # shake off any visual artifacts like previous highlighted cursor
            # position.
            self.wibble_wobble()
