from sublime import load_settings
from sublime import save_settings
from sublime import status_message
import sublime_plugin


def _load_preferences():
    return load_settings('Preferences.sublime-settings')


def _save_preferences():
    return save_settings('Preferences.sublime-settings')


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
        view = self.window.active_view()
        indent_guide_options = view.settings().get('indent_guide_options_default') if view else None
        if indent_guide_options:
            return indent_guide_options
        else:
            return [
                'draw_normal',
                'draw_active'
            ]


class ToggleInvisiblesCommand(ToggleCommand):

    def get_preference_name(self):
        return 'draw_white_space'

    def get_disable_value(self):
        view = self.window.active_view()
        draw_white_space = view.settings().get('draw_white_space_disabled_default') if view else None
        if draw_white_space:
            return draw_white_space

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
