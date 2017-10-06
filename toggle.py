from sublime import load_settings
from sublime import save_settings
from sublime_plugin import WindowCommand
from sublime_plugin import ApplicationCommand


class ToggleUserSettingCommand(ApplicationCommand):

    def run(self, key):
        settings = load_settings('Preferences.sublime-settings')
        settings = settings.set(key, not bool(settings.get(key, False)))
        save_settings('Preferences.sublime-settings')


class ToggleCommand(WindowCommand):

    def run(self):
        setting_name = self.get_setting_name()
        settings = load_settings('Preferences.sublime-settings')
        if settings.get(setting_name) != self.get_enabled_value():
            setting_value = self.get_enabled_value()
        else:
            setting_value = self.get_disable_value()
        settings.set(setting_name, setting_value)
        save_settings('Preferences.sublime-settings')

    def description(self):
        view = self.window.active_view()
        if view:
            current_value = view.settings().get(self.get_setting_name())
            if current_value == self.get_disable_value():
                return 'Show ' + self.get_setting_description()
            if current_value == self.get_enabled_value():
                return 'Hide ' + self.get_setting_description()

        return 'Toggle ' + self.get_setting_description()

    def get_setting_name(self):
        return self.name()[7:]

    def get_setting_description(self):
        return self.get_setting_name().replace('_', ' ').title()

    def get_disable_value(self):
        return False

    def get_enabled_value(self):
        return True


class ToggleFoldButtonsCommand(ToggleCommand):
    pass


class ToggleHighlightLineCommand(ToggleCommand):
    pass


class ToggleIndentGuideCommand(ToggleCommand):

    def get_setting_name(self):
        return 'indent_guide_options'

    def get_setting_description(self):
        return 'Indent Guide'

    def get_disable_value(self):
        return []

    def get_enabled_value(self):
        return ['draw_normal', 'draw_active']


class ToggleInvisiblesCommand(ToggleCommand):

    def get_setting_name(self):
        return 'draw_white_space'

    def get_disable_value(self):
        return 'selection'

    def get_enabled_value(self):
        return 'all'


class ToggleLineNumbersCommand(ToggleCommand):
    pass


class TogglePreviewOnClickCommand(ToggleCommand):

    def get_setting_description(self):
        return 'Preview on Click'


class ToggleRulersCommand(ToggleCommand):

    def get_disable_value(self):
        return []

    def get_enabled_value(self):
        return [80, 120]


class ToggleSaveOnFocusLostCommand(ToggleCommand):
    pass
