# gerardroche/sublime-polyfill

Plugin for Sublime Text 3. Inspired by Vim NERDTree and Vim CtrlP.

## Overview

* [Features](#features)
* [Commands](#commands)
* [Key Bindings](#key-bindings)
* [Configuration](#configuration)
* [Installation](#installation)
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

**Tree View**

* `,d` toggle sidebar **(vi_tree_view_toggle mode)**
* `a` add file **(experimental feature)**
* `A` add folder **(experimental feature)**
* `ctrl+\` reveal active file
* `d` duplicate **(experimental feature)**
* `f` find in files **(experimental feature)**
* `h` close node / go to parent node
* `i` open in split **(experimental feature)** *(not implemented yet)* #1
* `j` down
* `J` go to last child
* `k` up
* `l` open node
* `m` or `f2` move/rename **(experimental feature)**
* `p` go to parent node
* `P` go to root node
* `q` close
* `s` open in vsplit **(experimental feature)** *(not implemented yet)* #1
* `t` open in tab **(experimental feature)** *(not implemented yet)* #1

**Overlay**

* `ctrl+i` open in split **(experimental feature)** *(not implemented yet)* #2
* `ctrl+j` down
* `ctrl+k` up
* `ctrl+s` open in vsplit **(experimental feature)** *(not implemented yet)* #2
* `ctrl+t` open in tab **(experimental feature)** *(not implemented yet)* #2

**Autocomplete popup**

* `ctrl+n` or `ctrl+j` next / down
* `ctrl+p` or `ctrl+k` previous / up

## Configuration

`polyfill.experimental_features` `<bool>` Default is false

`polyfill.vi_tree_view_toggle` `<bool>` Default is false

## Installation

**Dependencies**

* Sublime Text `>=3095`
* [SidebarEnhancements](https://packagecontrol.io/packages/SideBarEnhancements) `>=st3#a307090`
* Some features only work with [Vintageous](https://packagecontrol.io/packages/Vintageous) `^4.0.3`

**Installation**

1. Close Sublime Text
2. Download or clone this repository to a directory named `polyfill` in the Sublime Text Packages directory for platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/.config/sublime-text-3/Packages/polyfill`
    * OS X: `git clone https://github.com/gerardroche/sublime-polyfill.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/polyfill`
    * Windows: `git clone https://github.com/gerardroche/sublime-polyfill.git %APPDATA%\Sublime/ Text/ 3/Packages/polyfill`
3. Done

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [BSD 3-Clause License](LICENSE).
