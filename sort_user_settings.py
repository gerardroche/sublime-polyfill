import sublime
import sublime_plugin


class SortUserSettingsCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('Preferences.sublime-settings')

        # ignored_packages
        ignored_packages = settings.get('ignored_packages', [])
        ignored_packages.sort()
        settings.set('ignored_packages', ignored_packages)

        # index_exclude_patterns
        index_exclude_patterns = settings.get('index_exclude_patterns', [])
        index_exclude_patterns.sort()
        settings.set('index_exclude_patterns', index_exclude_patterns)

        # file_exclude_patterns
        file_exclude_patterns = settings.get('file_exclude_patterns', [])
        file_exclude_patterns.sort()
        settings.set('file_exclude_patterns', file_exclude_patterns)

        # folder_exclude_patterns
        folder_exclude_patterns = settings.get('folder_exclude_patterns', [])
        folder_exclude_patterns.sort()
        settings.set('folder_exclude_patterns', folder_exclude_patterns)

        sublime.save_settings('Preferences.sublime-settings')
