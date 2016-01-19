# gerardroche/sublime-polyfill

A plugin for Sublime Text. Inspired by [scrooloose/nerdtree](https://github.com/scrooloose/nerdtree) and [kien/ctrlp.vim](https://github.com/kien/ctrlp.vim).

**Sublime Text 3 only**

## Overview

* [Features](#features)
* [Commands](#commands)
* [Key Bindings](#key-bindings)
* [Configuration](#configuration)
* [Installation](#installation)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

## Features

* Navigate sidebar with `j` and `k`
* Navigate sidebar nodes with go to parent node `p`, root `P`, last `J`, and more
* Navigate overlays and popups with `ctrl+j` and `ctrl+k`
* Navigate autocomplete popup with `ctrl+n` and `ctrl+p`
* Toggle sidebar with `,d` when using *Vintage/Vintageous*
* Toggle indent guides command, and line numbers, rulers, invisibles, and more
* Open recent project command, Sort user settings command, and more

## Commands

* `Application: Close Window`
* `Application: New File`
* `Application: New Window`
* `Application: Open File`
* `Application: Open Folder`
* `Application: Quit`
* `Project: Open Recent`
* `Project: Open`
* `Project: Switch`
* `Sort User Settings`
* `Toggle Indent Guides`
* `Toggle Invisibles`
* `Toggle Line Numbers`
* `Toggle Preview on Click`
* `Toggle Rulers`
* `Toggle Save on Lost Focus`
* `View: Groups: Move File to New Group`

## Key Bindings

### Tree View

Key | Description
--- | -----------
`j` | down
`k` | up
`ctrl+\` | reveal active file
`q` | close sidebar
`,d` | toggle sidebar in *vintage/vintageous*
`h` | close node / go to parent node
`l` | open node
`p` | go to parent node
`P` | go to root node
`J` | go to last child

*The following tree view keymaps are not enabled by default. Set `polyfill.experimental_features` to true to enable them. See the configuration section for more details.*

Key | Description
--- | -----------
`a` | add file
`A` | add folder
`d` | duplicate
`f` | find in files
`m` or `f2` | move/rename
`i` | open in split *(not implemented yet)* [#1](https://github.com/gerardroche/sublime-polyfill/issues/1)
`s` | open in vsplit *(not implemented yet)* [#1](https://github.com/gerardroche/sublime-polyfill/issues/1)
`t` | open in tab *(not implemented yet)* [#1](https://github.com/gerardroche/sublime-polyfill/issues/1)

### Overlay

Key | Description
--- | -----------
`ctrl+j` | down
`ctrl+k` | up
`ctrl+i` | open in split (requires [Origami], see [Installation](#dependencies))
`ctrl+s` | open in vsplit (requires [Origami], see [Installation](#dependencies))
`ctrl+t` | open in tab

### Autocomplete popup

Key | Description
--- | -----------
`ctrl+j` or `ctrl+n` | down / next
`ctrl+k` or `ctrl+p` | up / previous

## Configuration

Some features are considered experimental and require the "experimental_features" settings to be enabled.

### Settings

**polyfill.experimental_features**

Enable/disable features considuered experimental.

Type: `<bool>`

Default: `false`


**polyfill.vi_tree_view_toggle**

Type: <bool>`

Default: true

Enable/disable the vi tree view toggle feature.

## Installation

### Dependencies

* Requires Sublime Text `>=3083`.
* Some features require [SidebarEnhancements] `>=st3#a307090`.
* Some features require [Vintageous] `~4.0`.
* Some features require [Origami].

Some features are considered experimental and require the "experimental_features" settings to be enabled. These features are disabled by default. See [Configurations](#configuration) for more details.

### Package Control installation

The preferred method of installation is via Package Control.

1. Install [Package Control](https://packagecontrol.io).
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> (Windows, Linux) or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `polyfill` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text to complete installation. The features listed above should now be available.

### Manual installation

1. Close Sublime Text.
2. Download or clone this repository to a directory named `polyfill` in the Sublime Text Packages directory for your platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/.config/sublime-text-3/Packages/polyfill`
    * OS X: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/polyfill`
    * Windows: `git clone https://github.com/gerardroche/sublime-polyfill.git %APPDATA%\Sublime/ Text/ 3/Packages/polyfill`
3. Restart Sublime Text to complete installation. The features listed above should now be available.

## Contributing

Your issue reports and pull requests are always welcome.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).

[Origami]: https://github.com/SublimeText/Origami
[SidebarEnhancements]: https://packagecontrol.io/packages/SideBarEnhancements
[Vintageous]: https://packagecontrol.io/packages/Vintageous
