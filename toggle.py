import sublime
import sublime_plugin

class ToggleCommand(sublime_plugin.WindowCommand):

    def run(self):
        settings = sublime.load_settings('Preferences.sublime-settings')

        setting_name = self.setting_name()

        if settings.get(setting_name) != self.setting_enabled_value():
            setting_value = self.setting_enabled_value()
        else:
            setting_value = self.setting_disabled_value()

        settings.set(setting_name, setting_value)

        # for window in sublime.windows():
        #     for view in window.views():
        #         view.settings().set(setting_name, setting_value)

        sublime.save_settings('Preferences.sublime-settings')

    def description(self):
        view = self.window.active_view()
        if view != None:

            current_value = view.settings().get(self.setting_name())

            if current_value == self.setting_disabled_value():
                return 'Show ' + self.setting_description_title()

            if current_value == self.setting_enabled_value():
                return 'Hide ' + self.setting_description_title()

        return 'Toggle ' + self.setting_description_title()

    def setting_name(self):
        return self.name()[7:]

    def setting_enabled_value(self):
        return True

    def setting_disabled_value(self):
        return False

    def setting_description_title(self):
        return self.setting_name().replace('_', ' ').title()

class ToggleIndentGuideCommand(ToggleCommand):

    def setting_name(self):
        return 'indent_guide_options'

    def setting_disabled_value(self):
        return []

    def setting_enabled_value(self):
        return ['draw_normal', 'draw_active']

    def setting_description_title(self):
        return 'Indent Guide'

class ToggleInvisiblesCommand(ToggleCommand):

    def setting_name(self):
        return 'draw_white_space'

    def setting_disabled_value(self):
        return 'selection'

    def setting_enabled_value(self):
        return 'all'

class ToggleRulersCommand(ToggleCommand):

    def setting_disabled_value(self):
        return []

    def setting_enabled_value(self):
        return [80, 120]

class ToggleLineNumbersCommand(ToggleCommand):
    pass

class TogglePreviewOnClickCommand(ToggleCommand):
    pass
