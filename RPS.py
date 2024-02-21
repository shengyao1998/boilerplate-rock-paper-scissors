# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
hashmap = {}

def player(prev_play, opponent_history=[]):
    
    # Pattern length
    n = 5

    # Assume Bot First Play is always Rock
    # Append the prev_play into play history
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    # Assuming Bot Next Play is Paper if history play < 5
    next_play = 'P'

    if len(opponent_history) > n:
        # Get last n play history of opponent
        pattern = "".join(opponent_history[-n:])

        # Update the pattern.
        # See how frequent opponent use this pattern
        if pattern in hashmap.keys():
            hashmap[pattern] += 1
        else:
            hashmap[pattern] = 1

        potential_play = [(pattern[1:] + x) for x in ['R','P','S']]
        potential_pattern = {k: hashmap[k] for k in potential_play if k in hashmap}

        if potential_pattern:
            next_play = max(potential_pattern, key=potential_pattern.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[next_play]