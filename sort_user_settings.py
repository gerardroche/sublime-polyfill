import sublime
import sublime_plugin

def sort_user_settings(settings):

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

class SortUserSettingsCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('Preferences.sublime-settings')
        sort_user_settings(settings)
        sublime.save_settings('Preferences.sublime-settings')

# class SortUserSettingsListener():

#     def __init__(self):
#         self.settings = sublime.load_settings('Preferences.sublime-settings')
#         self.settings.clear_on_change('sort-preferences')
#         self.settings.add_on_change('sort-preferences', self.run)

#     def run(self):
#         sort_user_settings(self.settings)
#         # This breaks in Package Control 3 when trying to save; preferences get corrupted
#         # sublime.save_settings('Preferences.sublime-settings')

# def plugin_loaded():
#     settings = sublime.load_settings('Preferences.sublime-settings')
#     if settings.get('sort_user_settings_listener_enabled'):
#         SortUserSettingsListener()
