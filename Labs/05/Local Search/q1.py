def evaluate_hypothesis(hypothesis, examples, target_attr):
    score = 0
    for example in examples:
        if all(cond in example.items() for cond in hypothesis.items()):
            score += 1
    return score

def learn_rule(target_attr, attributes, examples, k):
    best_hypothesis = {}  # Start with the broadest possible hypothesis
    candidates = [best_hypothesis]

    while candidates:
        constraints = []
        for attr in attributes:
            for example in examples:
                constraints.append({attr: example[attr]})

        new_candidates = []
        for h in candidates:
            for c in constraints:
                new_hypothesis = h.copy()
                new_hypothesis.update(c)

                if new_hypothesis not in new_candidates:
                    new_candidates.append(new_hypothesis)

        for h in new_candidates:
            if evaluate_hypothesis(h, examples, target_attr) > evaluate_hypothesis(best_hypothesis, examples, target_attr):
                best_hypothesis = h

        candidates = sorted(
            new_candidates,
            key=lambda h: evaluate_hypothesis(h, examples, target_attr),
            reverse=True
        )[:k]

    possible_predictions = [
        example[target_attr] for example in examples
        if all(cond in example.items() for cond in best_hypothesis.items())
    ]
    prediction = max(set(possible_predictions), key=possible_predictions.count)

    return f"IF {best_hypothesis} THEN {prediction}"

game_state = [
    {"piece": "knight", "position": "f3", "score": 3},
    {"piece": "queen", "position": "d1", "score": 9},
    {"piece": "pawn", "position": "e4", "score": 1}
]
attributes = ["piece", "position"]
target_attr = "score"
k = 2

print(learn_rule(target_attr, attributes, game_state, k))
