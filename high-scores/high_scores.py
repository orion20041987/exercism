def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    max_3 = []
    try:
        for counter in range(3):
            max_3.append(scores[scores.index(max(scores))])
            scores.pop(scores.index(max(scores)))
            counter += 1
    except:
        pass

    return max_3
