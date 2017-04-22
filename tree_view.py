# Inspired By:
# * Vim CtrlP: https://kien.github.io/ctrlp.vim/
# * Vim NERDTree: http://www.vim.org/scripts/script.php?script_id=1658
# See also hjkl navigation http://stackoverflow.com/a/17573049

import sublime
import sublime_plugin


class TreeView():

    # @todo optimise configuration handling
    def load_preferences(self):
        return sublime.load_settings('Preferences.sublime-settings')

    def save_preferences(self):
        sublime.save_settings('Preferences.sublime-settings')

    def wibble_wobble(self):
        # Workaround ST API
        #
        # * Helps scroll active file into view
        # * Helps shakes off previous sidebar (highlighted) cursor position
        self.window.run_command('move', {'by': 'lines', 'forward': True})
        self.window.run_command('move', {'by': 'lines', 'forward': False})

    def ensure_file_under_cursor_is_open(self):
        preferences = self.load_preferences()
        self.preview_on_click = preferences.get('preview_on_click')

        if not self.preview_on_click:
            preferences.set('preview_on_click', True)
            self.save_preferences()

        self.wibble_wobble()

    def ensure_file_under_cursor_is_open_cleanup(self):
        if not self.preview_on_click:
            preferences = self.load_preferences()
            preferences.set('preview_on_click', False)
            self.save_preferences()
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
    """Inspired by Vim CtrlP https://kien.github.io/ctrlp.vim/"""

    def run(self, tab=None, split=None, vsplit=None):
        """
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
