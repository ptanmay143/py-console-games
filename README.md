# Python Console Games

> Command line interface games

![Dumb Tic Tac Toe](/assets/dumb-tic-tac-toe.png?raw=true)

- [Python Console Games](#python-console-games)
  - [Instructions](#instructions)
    - [Setup](#setup)
    - [Usage](#usage)

## Instructions

### Setup

- Install [Git-SCM](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

- Clone this repository and change directory to the cloned folder.

  ```powershell
  git clone https://github.com/ptanmay143/py-console-games.git
  Set-Location .\py-console-games\
  ```

- Install [Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

- Create a new conda environment with the name `py-console-games` and install the required dependencies.

  ```powershell
  conda create -n py-console-games python colorama termcolor
  ```

### Usage

- Activate the conda environment.

  ```powershell
  conda activate py-console-games
  ```

- Run the `dumb-tic-tac-toe.py` python script to play a game of tic tac toe.

  ```powershell
  python .\dumb-tic-tac-toe.py
  ```

- Run the `rock-paper-scissor.py` python script to play a game of rock, paper and scissor.

  ```powershell
  python .\rock-paper-scissor.py
  ```
