import sublime
import sublime_plugin

class ToggleCommand(sublime_plugin.WindowCommand):

    def run(self):
        setting_name = self.setting_name()
        settings = sublime.load_settings('Preferences.sublime-settings')
        if settings.get(setting_name) != self.setting_enabled_value():
            setting_value = self.setting_enabled_value()
        else:
            setting_value = self.setting_disabled_value()
        settings.set(setting_name, setting_value)
        sublime.save_settings('Preferences.sublime-settings')

    def description(self):
        view = self.window.active_view()
        if view:
            current_value = view.settings().get(self.setting_name())
            if current_value == self.setting_disabled_value():
                return 'Show ' + self.setting_description()
            if current_value == self.setting_enabled_value():
                return 'Hide ' + self.setting_description()

        return 'Toggle ' + self.setting_description()

    def setting_name(self):
        return self.name()[7:]

    def setting_description(self):
        return self.setting_name().replace('_', ' ').title()

    def setting_disabled_value(self):
        return False

    def setting_enabled_value(self):
        return True

class ToggleIndentGuideCommand(ToggleCommand):
    def setting_name(self):
        return 'indent_guide_options'

    def setting_description(self):
        return 'Indent Guide'

    def setting_disabled_value(self):
        return []

    def setting_enabled_value(self):
        return ['draw_normal', 'draw_active']

class ToggleInvisiblesCommand(ToggleCommand):
    def setting_name(self):
        return 'draw_white_space'

    def setting_disabled_value(self):
        return 'selection'

    def setting_enabled_value(self):
        return 'all'

class ToggleLineNumbersCommand(ToggleCommand):
    pass

class TogglePreviewOnClickCommand(ToggleCommand):

    def setting_description(self):
        return 'Preview on Click'

class ToggleRulersCommand(ToggleCommand):
    def setting_disabled_value(self):
        return []

    def setting_enabled_value(self):
        return [80, 120]

class ToggleSaveOnFocusLostCommand(ToggleCommand):
    pass
