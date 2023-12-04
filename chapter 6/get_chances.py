def calculate_chances(spread_factor, distance_factor):
    assert spread_factor > 1

    default_chance = 100 / (len(groups) * spread_factor)
    chances = [default_chance] * len(groups)

    # print(f'Chances before distribution: {chances}')
    # print(sum(chances))

    for i in range(1, len(groups) + 1):
        spacefac = default_chance / i
        for j in range(i - 1, -1, -1):
            chances[j] += spacefac * spread_factor * distance_factor

    chances[0] += 100 - sum(chances)
    per_xeno = {key: round(chances[i] / groups[key],2) for i, key in zip(range(len(chances)), groups)}

    print(f'Chances after distribution: {chances}')
    print(f'Chances per pawn xeno group: {per_xeno}')
    print(f'Total: {sum(chances)} %')


groups = {'Common': 2,
          'Uncommon': 5,
          'Rare': 6,
          'Epic': 7,
          'Legendary': 5,
          'Myths': 6}

spread_factor = 300  # the more this value is, the bigger is the difference between chances of the first and the last group
distance_factor = 0.9  # the closer this value to 1 is, the smaller the difference between the chances for first two groups
calculate_chances(spread_factor, distance_factor)
