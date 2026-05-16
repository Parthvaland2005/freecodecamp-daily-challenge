def get_longest_chain(dominoes):

    best_chain = []

    def backtrack(chain, remaining):

        nonlocal best_chain

        if len(chain) > len(best_chain):
            best_chain = chain[:]

        if not chain:

            for i, (a, b) in enumerate(remaining):

                backtrack(chain + [[a, b]],
                          remaining[:i] + remaining[i+1:])

                if a != b:
                    backtrack(chain + [[b, a]],
                              remaining[:i] + remaining[i+1:])

        else:

            last = chain[-1][1]

            for i, (a, b) in enumerate(remaining):

                if a == last:
                    backtrack(chain + [[a, b]],
                              remaining[:i] + remaining[i+1:])

                if b == last and a != b:
                    backtrack(chain + [[b, a]],
                              remaining[:i] + remaining[i+1:])

    backtrack([], dominoes)

    return best_chain

print(get_longest_chain([[1, 2], [4, 5], [2, 3]]))

print(get_longest_chain([[2, 1], [4, 3], [5, 3]]))

print(get_longest_chain([[1, 2], [3, 4], [2, 3], [4, 0]]))

print(get_longest_chain([
    [6, 6], [6, 1], [1, 1],
    [0, 3], [2, 3], [4, 1], [5, 6]
]))

print(get_longest_chain([
    [0, 4], [3, 3], [0, 3],
    [5, 6], [4, 5], [4, 2],
    [5, 5], [1, 2], [4, 4]
]))