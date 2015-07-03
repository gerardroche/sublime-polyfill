import sublime_plugin

class OverlayOpenFileCommand(sublime_plugin.WindowCommand):

    """
    Open File

    Inspired by Vim CtrlP https://kien.github.io/ctrlp.vim/
    """

    def run(self, tab = None, split = None, vsplit = None):
        """
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
            return bool(view.settings().get('tweaks.experimental_features'))
        return False

    # @todo open overlay view file in vertical split
    def open_file_in_vertical_split(self, fname):
        self.window.open_file(fname)

    # @todo open overlay view file in horizontal split
    def open_file_in_horizontal_split(self, fname):
        self.window.open_file(fname)

    # @todo open overlay view file in tab
    def open_file_in_tab(self, fname):
        self.window.open_file(fname)
