# WHAT POLYFILL IS

[![Minimum Sublime Version](https://img.shields.io/badge/sublime-%3E%3D%203.0-brightgreen.svg?style=flat-square)](https://sublimetext.com) [![Latest Stable Version](https://img.shields.io/github/tag/gerardroche/sublime-polyfill.svg?style=flat-square&label=stable)](https://github.com/gerardroche/sublime-polyfill/tags) [![GitHub stars](https://img.shields.io/github/stars/gerardroche/sublime-polyfill.svg?style=flat-square)](https://github.com/gerardroche/sublime-polyfill/stargazers) [![Downloads](https://img.shields.io/packagecontrol/dt/polyfill.svg?style=flat-square)](https://packagecontrol.io/packages/polyfill) [![Author](https://img.shields.io/badge/twitter-gerardroche-blue.svg?style=flat-square)](https://twitter.com/gerardroche)

Polyfill is a collection of fixes, commands, and other features for Sublime Text. It is inspired by Vim plugins such as [nerdtree](https://github.com/scrooloose/nerdtree) and [ctrlp.vim](https://github.com/kien/ctrlp.vim).

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

* Navigate sidebar (tree view) with `j` and `k`
* Navigate sidebar (tree view) nodes with go to parent node `p`, root `P`, last `J`, and more
* Navigate overlays and pop-ups with `ctrl+j` and `ctrl+k`
* Navigate auto-complete pop-up with `ctrl+n` and `ctrl+p`
* Toggle sidebar with `,d` when using *Vintage/Vintageous*
* Toggle indent guides command, and line numbers, rulers, invisibles, and more
* Open recent project command, Sort user settings command, and more

## COMMANDS

* `Application: Clear Window`
* `Application: Close Window`
* `Application: Enable Color Scheme`
* `Application: Enable Theme`
* `Application: New File`
* `Application: New Window`
* `Application: Open File`
* `Application: Open Folder`
* `Application: Quit`
* `Application: Reset Window`
* `Project: Open Recent`
* `Project: Open`
* `Project: Switch`
* `Resize Groups Almost Equally`
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
<kbd>j</kbd> | down
<kbd>k</kbd> | up
<kbd>ctrl+\</kbd> | reveal active file
<kbd>q</kbd> | close sidebar
<kbd>,d</kbd> | toggle sidebar in *vintage/vintageous*
<kbd>h</kbd> | close node / go to parent node
<kbd>l</kbd> | open node
<kbd>p</kbd> | go to parent node
<kbd>P</kbd> | go to root node
<kbd>J</kbd> | go to last child

*The following tree view keymaps are not enabled by default. Set `polyfill.experimental_features` to true to enable them. See the configuration section for more details.*

Key | Description
--- | -----------
<kbd>a</kbd> | add file
<kbd>A</kbd> | add folder
<kbd>d</kbd> | duplicate
<kbd>f</kbd> | find in files
<kbd>m</kbd> or <kbd>f2</kbd> | move/rename
<kbd>i</kbd> | open in split *(not implemented yet)* [#1](https://github.com/gerardroche/sublime-polyfill/issues/1)
<kbd>s</kbd> | open in vsplit *(not implemented yet)* [#1](https://github.com/gerardroche/sublime-polyfill/issues/1)
<kbd>t</kbd> | open in tab *(not implemented yet)* [#1](https://github.com/gerardroche/sublime-polyfill/issues/1)

### Overlay

Key | Description
--- | -----------
<kbd>ctrl+j</kbd> | down
<kbd>ctrl+k</kbd> | up
<kbd>ctrl+i</kbd> | open in split (requires [Origami], see [Installation](#dependencies))
<kbd>ctrl+s</kbd> | open in vsplit (requires [Origami], see [Installation](#dependencies))
<kbd>ctrl+t</kbd> | open in tab

### Auto-complete pop-up

Key | Description
--- | -----------
<kbd>ctrl+j</kbd> or <kbd>ctrl+n</kbd> | down / next
<kbd>ctrl+k</kbd> or <kbd>ctrl+p</kbd> | up / previous

## CONFIGURATION

Some features are considered experimental and require the "experimental_features" settings to be enabled.

Key | Description | Type | Default
----|-------------|------|--------
`polyfill.experimental_features` | Enable experimental features. | `boolean` | `false`
`polyfill.keymaps` | Disable the default keymaps. | `boolean` | `true`
`polyfill.vi_tree_view_toggle` | Enable vi tree view toggle. | `boolean` | `true`

### User Settings

`Preferences > Settings - User`

```json
{
    "polyfill.{Key}": "{Value}"
}
```

### Per-Project Settings

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

* Some features require [NeoVintageous] `~1.0`.
* Some features require [Origami].

### Package Control installation

The preferred method of installation is [Package Control](https://packagecontrol.io/browse/authors/gerardroche).

### Manual installation

Close Sublime Text then download or clone this repository to a directory named `polyfill` in the Sublime Text Packages directory for your platform:

* Linux: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/.config/sublime-text-3/Packages/polyfill`
* OSX: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/polyfill`
* Windows: `git clone https://github.com/gerardroche/sublime-polyfill.git %APPDATA%\Sublime/ Text/ 3/Packages/polyfill`

## CONTRIBUTING

Your issue reports and pull requests are always welcome.

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md).

## LICENSE

Released under the [BSD 3-Clause License](LICENSE).

[Origami]: https://github.com/SublimeText/Origami
[NeoVintageous]: https://packagecontrol.io/packages/NeoVintageous
