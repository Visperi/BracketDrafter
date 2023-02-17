import random
import argparse
from typing import List

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def read_player_file(filepath: str) -> List[str]:
    with open(filepath, "r") as players_file:
        return players_file.read().splitlines()


def draft_group(group_size: int, _players: List[str]) -> List[str]:
    group = []
    remaining_players = _players.copy()

    while len(group) != group_size:
        random_player = random.choice(remaining_players)
        remaining_players.remove(random_player)
        group.append(random_player)

    return group


def draft_groups(group_size: int, group_amount: int, _players: List[str]) -> List[List[str]]:
    if group_size < 1:
        raise ValueError("Group size must be greater than zero")
    if group_amount < 1:
        raise ValueError("Group amount must be greater than zero")
    if len(_players) < 2:
        return [_players]

    groups = []
    remaining_players = _players.copy()

    for _ in range(group_amount):
        group = draft_group(group_size, remaining_players)
        remaining_players = [player for player in _players if player not in group]
        groups.append(group)

    return groups


def parse_arguments(**kwargs) -> argparse.Namespace:
    parser = argparse.ArgumentParser(**kwargs)

    parser.add_argument("--pfile", "--player-file",
                        type=str,
                        help="Configure a file where players are read from. Default value: players.txt")
    parser.add_argument("--gamount", "--group-amount",
                        type=int,
                        help="Configure amount of groups in the tournament. Default value: 2")
    parser.add_argument("--gsize", "--group-size",
                        type=int,
                        help="Configure the tournament group sizes. Default value: the players amount divided by "
                             "the group amount floored down, with minimum value of 1")

    return parser.parse_args()


def parse_left_out_players(players, groups) -> List[str]:
    flattened_groups = []
    for group in groups:
        for player in group:
            flattened_groups.append(player)

    return [player for player in players if player not in flattened_groups]


if __name__ == "__main__":
    args = parse_arguments()

    players_file_path = args.pfile or "players.txt"
    _players = read_player_file(players_file_path)

    _group_amount = args.gamount or 2
    _group_size = args.gsize or max(len(_players) // _group_amount, 1)

    _players = read_player_file(players_file_path)
    _groups = draft_groups(_group_size, _group_amount, _players)
    for i, _group in enumerate(_groups):
        print(f"\nGROUP {ALPHABET[i]}:")
        print("\n".join(_group))

    if len(_players) % _group_amount != 0:
        left_out_players = parse_left_out_players(_players, _groups)
        print(f"\nFollowing players did not fit into evenly divided groups: {left_out_players}")
