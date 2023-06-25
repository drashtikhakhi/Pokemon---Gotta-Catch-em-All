# Pokemon---Gotta-Catch-Them-All

### Introduction
This is a text-based game created in Python. It is a single-player puzzle game where the objective is for the player to find
all the Pokemon without scaring them away by stepping on them. When the game starts the player should first be prompted for the game size (i.e. the grid size), before being prompted for the number of Pokemons used in the game. The game should then be displayed with all tiles unexposed. At every turn, the player will be prompted for an action.

##### List of valid Actions
| Input  | Action | Example |
| --------------------------------- | -------------------- | ---- |
|   -Upper Case Character--number-  |     Select a cell    |  A1  | 
| f -Upper Case Character--number-  | Place/remove a flag  | f A1 |
|                 h                 |      Help text       |  'h' |
|                 q                 |         Quit         |  'q' |
|                ':)'               |        Restart       | ':)' |

##### Example

- Please input the size of the grid: 5
- Please input the number of pokemons: 5

|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | ~ | ~ | ~ | ~ | ~ |
B | ~ | ~ | ~ | ~ | ~ |
C | ~ | ~ | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | ~ |

Please input action: A1
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 1 | ~ | ~ | ~ | ~ |
B | ~ | ~ | ~ | ~ | ~ |
C | ~ | ~ | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | ~ |

Please input action: E5
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 1 | ~ | ~ | ~ | ~ |
B | ~ | ~ | ~ | ~ | ~ |
C | ~ | ~ | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | 2 |

Please input action: h
- h - Help.
- <Uppercase Letter><number> - Selecting a cell (e.g. 'A1')
- f <Uppercase Letter><number> - Placing flag at cell (e.g. 'f A1')
- :) - Restart game.
- q - Quit.

|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 1 | ~ | ~ | ~ | ~ |
B | ~ | ~ | ~ | ~ | ~ |
C | ~ | ~ | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | 2 |

Please input action: :)
It's rewind time.
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | ~ | ~ | ~ | ~ | ~ |
B | ~ | ~ | ~ | ~ | ~ |
C | ~ | ~ | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | ~ |

Please input action: A1
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 0 | 1 | ~ | ~ | ~ |
B | 0 | 1 | ~ | ~ | ~ |
C | 1 | 2 | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | ~ |

Please input action: A4
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 0 | 1 | ~ | 2 | ~ |
B | 0 | 1 | ~ | ~ | ~ |
C | 1 | 2 | ~ | ~ | ~ |
D | ~ | ~ | ~ | ~ | ~ |
E | ~ | ~ | ~ | ~ | ~ |

Please input action: C5
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 0 | 1 | ~ | 2 | ~ |
B | 0 | 1 | ~ | 2 | 1 |
C | 1 | 2 | ~ | 1 | 0 |
D | ~ | ~ | ~ | 2 | 2 |
E | ~ | ~ | ~ | ~ | ~ |

Please input action: A5
|  | 1 | 2 | 3 | 4 | 5 |
|--|---|---|---|---|---|
A | 0 | 1 | ~ | 2 | :)|
B | 0 | 1 | :)| 2 | 1 |
C | 1 | 2 | ~ | 1 | 0 |
D | ~ | :)| ~ | 2 | 2 |
E | ~ | ~ | ~ | :)| :)|

You have scared away all the pokemons.
