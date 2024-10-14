import random

def player(prev_play, opponent_history=[]):
    
    if prev_play:
        opponent_history.append(prev_play)

    # Define available moves
    moves = ["R", "P", "S"]

    # Strategy State: Select the strategy based on observed patterns
    if len(opponent_history) < 10:
        # Early in the game, choose randomly or use a fallback strategy
        return random.choice(moves)
    
   
    sequence_length = 3
    if len(opponent_history) >= sequence_length:
        # Get recent pattern of opponent moves
        recent_sequence = "".join(opponent_history[-sequence_length:])

        # Search for this pattern in their history
        patterns = {}
        for i in range(len(opponent_history) - sequence_length):
            seq = "".join(opponent_history[i:i + sequence_length])
            next_move = opponent_history[i + sequence_length] if i + sequence_length < len(opponent_history) else None
            if seq in patterns:
                patterns[seq].append(next_move)
            else:
                patterns[seq] = [next_move]

        # Choose the next move based on the most frequent pattern
        if recent_sequence in patterns:
            next_moves = patterns[recent_sequence]
            if next_moves:
                most_likely_move = max(set(next_moves), key=next_moves.count)
                # Counter the most likely move
                if most_likely_move == "R":
                    return "P"  # Paper beats Rock
                elif most_likely_move == "P":
                    return "S"  # Scissors beat Paper
                elif most_likely_move == "S":
                    return "R"  # Rock beats Scissors

    # Default to a random choice if no patterns are detected
    return random.choice(moves)
