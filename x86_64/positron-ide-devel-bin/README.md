# positron-ide-devel-bin

<!-- badges: start -->
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![GPLv3 Licence Badge](https://img.shields.io/badge/license-GPLv3-bd0000.png)](https://www.gnu.org/licenses/gpl-3.0)
<!-- badges: end -->

## Overview

This repository contains a [PKGBUILD](https://wiki.archlinux.org/title/PKGBUILD) script for building and installing the [`positron-ide-devel-bin`](https://aur.archlinux.org/packages/positron-ide-devel-bin) package from the Arch User Repository ([AUR](https://aur.archlinux.org/)).

## Usage

To build and install the `positron-ide-devel-bin` package, follow these steps:

1. **Clone the Repository**: Open your terminal and run the following command to clone this repository:

```bash
  git clone https://github.com/ponte-vecchio/positron
```

2. **Navigate to the Directory**: Change into the cloned repository's directory:

```bash
  cd positron
```

3. **Build and Install the Package**: Use the `makepkg` command to build and install the package:

```bash
  makepkg -si
```

This command will download the necessary files, build the package, and install it on your system.

## Known Issues

### GitHub Copilot

GitHub Copilot may fail to authenticate on fresh installations of Positron IDE on Arch Linux. If you encounter issues, sign out of GitHub Copilot and sign back in to resolve the problem.

## Licence

[![Licence: GPLv3](https://img.shields.io/badge/license-GPLv3-bd0000.svg)](https://www.gnu.org/licenses/gpl-3.0)

```text
Copyright (C) 2026 Leothelion

positron-ide-devel-bin is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.
```