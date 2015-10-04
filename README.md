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
* Navigate sidebar nodes with go to parent node `p`, root `P`, and last `J`
* Navigate overlays with `ctrl+j` and `ctrl+k`
* Navigate autocomplete popup with `ctrl+n` or `ctrl+j`  and `ctrl+p` or `ctrl+k`
* Close sidebar `q`
* Close and open sidebar nodes with `h` and `l`
* Toggle sidebar in *Vi/Vintage/Vintageous* with `,d`
* Toggle indent guide, invisibles, line numbers, preview on click, rulers, and save on lost focus
* Open recent project
* Sort user settings

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

**Requirements**

* Sublime Text `>=3065`
* SidebarEnhancements `>=st3#a307090`
* Some features require Vintageous `^4.0.3`

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
