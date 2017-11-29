# POLYFILL CHANGELOG

All notable changes are documented in this file using the [Keep a CHANGELOG](http://keepachangelog.com/) principles.

## Unreleased

## Added

* Added: Sort User Settings command now sorts `added_words`
* Added: Status message for toggle commands
* Added: Toggle Fold Buttons command

## Changed

* Changed: `vi_tree_view_toggle` is now disabled by default

## Fixed

* Fixed: Several Sort User Settings command issues
* Fixed: Missing `vi_tree_toggle` context setting check
* Fixed: Edge-case issue enabling color scheme

## 1.6.0

### Added

* Added: Toggle Highlight Line command

## 1.5.0

### Added

* Added: Exclude themes/color-scheme in tests folders from enable theme/color-scheme command

### Fixed

* Fixed: Menu paths

## 1.4.0

### Added

* Added: Resize Groups Almost Equally command
* Added: Clear Window and Reset Window commands

## 1.3.0

### Added

* Added: Sort ignored words when sorting user preferences

## 1.2.0

### Added

* Added: Keymap for opening recent projects <kbd>Super+Alt+R</kbd> (OSX) <kbd>Ctrl+Alt+R</kbd> (Windows, Linux)

### Fixed

* Fixed: Don't show quick panel if only the current theme is available

## 1.1.0

### Added

* Added: "Application: Enable Theme" command
* Added: "Application: Enable Color Scheme" command
* Added: "toggle_user_setting <key>" command

## 1.0.0

### Added

* Added: Update README for 1.0.0 release

## 0.8.0

### Added

* Added: #2 open file from overlay in split with ctrl+s (requires Origami package)
* Added: #2 open file from overlay in vertical split with ctrl+v (requires Origami package)
* Added: #2 open file from overlay in tab with ctrl+t

## 0.7.1

### Fixed

* Fixed: Open recent project command was sometimes opening the wrong project

## 0.7.0

### Added

* Added: CHANGELOG link to package settings menu

### Changed

* Changed: Toggle sidebar in vintage/vintageous with ,d is now enabled by default

### Removed

* Removed: package control messages; it takes too much time to maintain these, see CHANGELOG

### Fixed

* Fixed: Open Recent Project command now only prompts to open recent projects that really exist

## 0.6.0

### Added

* Added: package control messages

## 0.5.0

### Fixed

* Fixed: Move active view into the new group of the new layout on ctrl+alt+{n} keymaps
* Fixed: Don't change focus when layout doesn't change on ctrl+alt+{n} keymaps

## 0.4.0

### Added

* Added: command palette: "View: Groups: Move File to New Group"

### Changed

* Changed: Renamed command file from "overlay.py" "overlay_open_file.py"

## 0.3.1

### Fixed

* Fixed: "Toggle Save on Focus Lost" should persist

## 0.3.0

### Added

* Added: "Toggle Save on Focus Lost" command

## 0.2.0

### Changed

* Changed: Renamed plugin from sublime-tweaks to sublime-polyfill

## 0.1.0

* Initial release
