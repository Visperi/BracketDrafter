# BracketDrafter

To generate brackets, just add `players.txt` to the project root folder and run the script. Group amount and group 
sizes can be adjusted using command line arguments. Optional argument `--help` prints argument descriptions.

### Running

`python bracket_drafter.py --player-file path/to/my/file --group-size 4 --group-amount 3`

Above parameters could output someting like this (assuming the file contains 13 players):

```
GROUP A:
player 6
player 1
player 13
player 5

GROUP B:
player 9
player 11
player 8
player 10

GROUP C:
player 12
player 7
player 4
player 3

Following players did not fit into evenly divided groups: ['player 2']
```