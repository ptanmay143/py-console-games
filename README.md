# Python Console Games

> Command line interface games

![Dumb Tic-Tac-Toe](/assets/dumb-tic-tac-toe.png?raw=true)

---

- [Python Console Games](#python-console-games)
  - [Instructions](#instructions)
    - [Setup](#setup)
    - [Usage](#usage)
  - [License](#license)

---

## Instructions

### Setup

- Install [Git-SCM](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

- Clone this repository and change directory to the cloned folder.

  ```shell
  git clone https://github.com/ptanmay143/py-console-games.git
  cd ./py-console-games/
  ```

- Install [Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Create a conda environment.

  ```shell
  conda create -n py-console-games
  ```

- Install required dependencies.

  ```shell
  conda env create -f ./environment.yml
  ```

### Usage

- Activate the conda environment.

  ```shell
  conda activate py-console-games
  ```

- Run the `dumb-tic-tac-toe.py` python script to play a game of tic-tac-toe.

  ```shell
  python ./dumb-tic-tac-toe.py
  ```

- Run the `rock-paper-scissor.py` python script to play a game of rock, paper and scissor.

  ```shell
  python ./rock-paper-scissor.py
  ```

---

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
