# sublime-tweaks

sublime-tweaks plugin for Sublime Text 3. Provides various Sublime Text tweaks and fixes.

## Overview

* [Features](#features)
* [Commands](#commands)
* [Key Bindings](#key-bindings)
* [Configuration](#configuration)
* [Installation](#installation)
* [Changelog](#changelog)
* [Credits](#credits)
* [License](#license)

## Features

* Navigate sidebar with `j` and `k`
* Navigate sidebar nodes with go to parent node `p`, root `P`, and last `J`
* Navigate overlays with `ctrl+j` and `ctrl+k`
* Navigate autocomplete popup with `ctrl+n` or `ctrl+j`  and `ctrl+p` or `ctrl+k`
* Close sidebar `q`
* Close and open sidebar nodes with `h` and `l`
* Toggle sidebar in *Vi/Vintage/Vintageous* with `,d`
* Toggle indent guides
* Toggle invisibles
* Toggle line numbers
* Toggle preview on click
* Toggle rulers
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

## Key Bindings

**Tree View**

* `,d` toggle sidebar **(vi_tree_view_toggle mode)**
* `a` add file **(experimental feature)**
* `A` add folder **(experimental feature)**
* `ctrl+\` reveal active file
* `d` duplicate **(experimental feature)**
* `h` close node / go to parent node
* `h` go to parent node / close node
* `i` open in split **(experimental feature)** *(not implemented yet)*
* `j` down
* `J` go to last child
* `k` up
* `l` open node
* `m` or `f2` move/rename **(experimental feature)**
* `p` go to parent node
* `P` go to root node
* `q` close
* `s` open in vsplit **(experimental feature)** *(not implemented yet)*
* `t` open in tab **(experimental feature)** *(not implemented yet)*

**Overlay**

* `ctrl+i` open in split **(experimental feature)** *(not implemented yet)*
* `ctrl+j` down
* `ctrl+k` up
* `ctrl+s` open in vsplit **(experimental feature)** *(not implemented yet)*
* `ctrl+t` open in tab **(experimental feature)** *(not implemented yet)*

**Autocomplete popup**

* `ctrl+n` or `ctrl+j` next / down
* `ctrl+p` or `ctrl+k` previous / up

## Configuration

`tweaks.experimental_features` `<bool>` Default is false

`tweaks.vi_tree_view_toggle` `<bool>` Default is false

## Installation

**Requires Sublime Text >= 3065**

1. Close Sublime Text
2. Download or clone this repository to a directory named `tweaks` in the Sublime Text Packages directory for platform:
    * Linux: `git clone https://github.com/gerardroche/sublime-tweaks.git ~/.config/sublime-text-3/Packages/tweaks`
    * OS X: `git clone https://github.com/gerardroche/sublime-tweaks.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/tweaks`
    * Windows: `git clone https://github.com/gerardroche/sublime-php-grammar.git %APPDATA%\Sublime/ Text/ 3/Packages/tweaks`
3. Done

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Credits

Inspired in part by Vim NERDTree and Vim CtrlP.

## License

sublime-tweaks is released under the [BSD 3-Clause License](LICENSE)
