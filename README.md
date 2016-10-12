# WHAT POLYFILL IS

[![Author](https://img.shields.io/badge/author-@gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche) [![Source Code](https://img.shields.io/badge/source-GitHub-blue.svg?style=flat-square)](https://github.com/gerardroche/sublime-polyfill) [![License](https://img.shields.io/badge/license-BSD--3-blue.svg?style=flat-square)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-polyfill.svg?style=flat-square)](https://github.com/gerardroche/sublime-polyfill/stargazers) [![Sublime version](https://img.shields.io/badge/sublime-v3.0.0-green.svg?style=flat-square)](https://sublimetext.com) [![Latest version](https://img.shields.io/github/tag/gerardroche/sublime-polyfill.svg?label=release&style=flat-square&maxAge=86400)](https://github.com/gerardroche/sublime-polyfill/tags) [![Downloads](https://img.shields.io/packagecontrol/dt/polyfill.svg?style=flat-square&maxAge=86400)](https://packagecontrol.io/packages/polyfill)

POLYFILL is a collection of fixes, commands, and other features for Sublime Text. It is inspired by Vim plugins such as [scrooloose/nerdtree](https://github.com/scrooloose/nerdtree) and [kien/ctrlp.vim](https://github.com/kien/ctrlp.vim).

## OVERVIEW

* [Features](#features)
* [Commands](#commands)
* [Key Bindings](#key-bindings)
* [Configuration](#configuration)
* [Installation](#installation)
* [Contributing](#contributing)
* [Changelog](#changelog)
* [License](#license)

## FEATURES

* Navigate sidebar with `j` and `k`
* Navigate sidebar nodes with go to parent node `p`, root `P`, last `J`, and more
* Navigate overlays and popups with `ctrl+j` and `ctrl+k`
* Navigate autocomplete popup with `ctrl+n` and `ctrl+p`
* Toggle sidebar with `,d` when using *Vintage/Vintageous*
* Toggle indent guides command, and line numbers, rulers, invisibles, and more
* Open recent project command, Sort user settings command, and more

## COMMANDS

* `Application: Close Window`
* `Application: Enable Color Scheme`
* `Application: Enable Theme`
* `Application: New File`
* `Application: New Window`
* `Application: Open File`
* `Application: Open Folder`
* `Application: Quit`
* `Project: Open Recent`
* `Project: Open`
* `Project: Switch`
* `Sort User Settings`
* `Toggle Indent Guide`
* `Toggle Invisibles`
* `Toggle Line Numbers`
* `Toggle Preview on Click`
* `Toggle Rulers`
* `Toggle Save on Lost Focus`
* `View: Groups: Move File to New Group`

## KEY BINDINGS

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

## CONFIGURATION

Some features are considered experimental and require the "experimental_features" settings to be enabled.

### Settings

Key | Description | Type | Default
----|-------------|------|--------
`polyfill.experimental_features` | Enable experimental features. | `boolean` | `false`
`polyfill.vi_tree_view_toggle` | Enable vi tree view toggle. | `boolean` | `true`

#### User Settings

`Preferences > Settings - User`

```json
{
    "polyfill.{Key}": "{Value}"
}
```

#### Per-Project Settings

`Project > Edit Project`

```json
{
    "settings": {
        "polyfill.{Key}": "{Value}"
    }
}
```

## INSTALLATION

Some features are considered experimental and require the "experimental_features" settings to be enabled. These features are disabled by default. See [Configurations](#configuration) for more details.

* Some features require [SidebarEnhancements] `>=st3#a307090`.
* Some features require [Vintageous] `~4.0`.
* Some features require [Origami].

### Package Control

The preferred method of installation is [Package Control].

### Manual

1. Close Sublime Text.
2. Download or clone this repository to a directory named **`polyfill`** in the Sublime Text Packages directory for your platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/.config/sublime-text-3/Packages/polyfill`
    * OS X: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/polyfill`
    * Windows: `git clone https://github.com/gerardroche/sublime-polyfill.git %APPDATA%\Sublime/ Text/ 3/Packages/polyfill`
3. Done!

## CONTRIBUTING

Your issue reports and pull requests are always welcome.

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).

[Package Control]: https://packagecontrol.io/browse/authors/gerardroche
[Origami]: https://github.com/SublimeText/Origami
[SidebarEnhancements]: https://packagecontrol.io/packages/SideBarEnhancements
[Vintageous]: https://packagecontrol.io/packages/Vintageous
