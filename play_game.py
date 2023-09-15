from random import choice
from tqdm import tqdm  # progress bar, can be removed


def smart_opponent(played_moves, initial_probabilities=None):
    if initial_probabilities is None:
        initial_probabilities = [1 / 7 for i in range(14)]

    assert abs(sum(initial_probabilities) - 1) < 0.000001, "initial probability must sum to 1"
    # not exactly equal to 1, to account for floating point error

    all_states = [[i, (i + 5) % 14] for i in range(14)]

    # the game board has 28 states in total,
    # as there are 14 choices for where the first hand is
    # and 2 where the other one is
    for move in played_moves:
        all_states = [i for i in all_states if move not in i]

    probs = [0 for i in range(len(initial_probabilities))]

    for state in all_states:
        for s in state:
            probs[s] += initial_probabilities[s]
    for move in played_moves:
        probs[move] = 1

    lowest_prob = probs[0]
    lowest_idx = 0
    for i in range(1, 10):
        if probs[i] < lowest_prob and i not in played_moves:
            lowest_prob = probs[i]
            lowest_idx = i
    return lowest_idx


def random_opponent(played_moves):
    return choice([i for i in range(10) if i not in played_moves])


def get_random_teeth():
    # this is purely random, but shouldn't be. FIXME?
    tooth = choice([i for i in range(14)])
    other = (tooth + choice([5, 9])) % 14
    return fix_length([tooth, other])


def fix_length(l, max=10):
    return list(filter(lambda x: x < max, l))


def play_game():
    # smart start
    total_smart_wins = 0
    total = 10 ** 6
    for i in tqdm(range(total)):
        teeth = get_random_teeth()
        played = []
        turn = 0
        lost = False
        while not lost:
            if turn % 2 == 0:
                guess = smart_opponent(played)
            else:
                guess = random_opponent(played)
            if guess in played:
                print("SOEMTHING WONG")
                print(played, turn, guess)
                return
            if guess in teeth:
                total_smart_wins += (turn % 2) == 1
                lost = True
            else:
                played.append(guess)
                turn += 1
    print(f"total win % for smart opponent when they start is {total_smart_wins / total}")
    # random start
    total_smart_wins = 0
    total = 10 ** 6
    for i in tqdm(range(total)):
        teeth = get_random_teeth()
        played = []
        turn = 0
        lost = False
        while not lost:
            if turn % 2 == 0:
                guess = random_opponent(played)
            else:
                guess = smart_opponent(played)
            if guess in played:
                print("SOEMTHING WONG")
                print(played, turn, guess)
                return
            if guess in teeth:
                total_smart_wins += (turn % 2) == 0
                lost = True
            else:
                played.append(guess)
                turn += 1
    print(f"total win % for smart opponent when they don't start is {total_smart_wins / total}")


if __name__ == '__main__':
    play_game()
