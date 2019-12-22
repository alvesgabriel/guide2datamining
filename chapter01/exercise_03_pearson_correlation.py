from math import sqrt

users = {
    'Angelica': {'Blues Traveler': 3.5, 'Broken Bells': 2.0, 'Norah Jones': 4.5, 'Phoenix': 5.0,
                 'Slightly Stoopid': 1.5, 'The Strokes': 2.5, 'Vampire Weekend': 2.0},
    'Bill': {'Blues Traveler': 2.0, 'Broken Bells': 3.5, 'Deadmau5': 4.0, 'Phoenix': 2.0, 'Slightly Stoopid': 3.5,
             'Vampire Weekend': 3.0},
    'Chan': {'Blues Traveler': 5.0, 'Broken Bells': 1.0, 'Deadmau5': 1.0, 'Norah Jones': 3.0, 'Phoenix': 5.0,
             'Slightly Stoopid': 1.0},
    'Dan': {'Blues Traveler': 3.0, 'Broken Bells': 4.0, 'Deadmau5': 4.5, 'Phoenix': 3.0, 'Slightly Stoopid': 4.5,
            'The Strokes': 4.0, 'Vampire Weekend': 2.0},
    'Hailey': {'Broken Bells': 4.0, 'Deadmau5': 1.0, 'Norah Jones': 4.0, 'The Strokes': 4.0, 'Vampire Weekend': 1.0},
    'Jordyn': {'Broken Bells': 4.5, 'Deadmau5': 4.0, 'Norah Jones': 5.0, 'Phoenix': 5.0, 'Slightly Stoopid': 4.5,
               'The Strokes': 4.0, 'Vampire Weekend': 4},
    'Sam': {'Blues Traveler': 5.0, 'Broken Bells': 2.0, 'Norah Jones': 3.0, 'Phoenix': 5.0, 'Slightly Stoopid': 4.0,
            'The Strokes': 5.0},
    'Veronica': {'Blues Traveler': 3.0, 'Norah Jones': 5.0, 'Phoenix': 4.0, 'Slightly Stoopid': 2.5,
                 'The Strokes': 3.0},
}


def pearson(user1, user2):
    '''>>> pearson(users['Angelica'], users['Bill'])
    -0.90405349906826993
    >>> pearson(users['Angelica'], users['Hailey'])
    0.42008402520840293
    >>> pearson(users['Angelica'], users['Jordyn'])
    0.76397486054754316
    '''
    rating1 = tuple(v for v in user1.values())
    rating2 = tuple(v for v in user2.values())
    sum_xy = sum((x * y for x, y in zip(rating1, rating2)))
    sum_x = sum(rating1)
    sum_y = sum(rating2)
    n = len(rating1)
    numerator = sum_xy - ((sum_x * sum_y) / n)
    sum_x2 = sum((x ** 2 for x in rating1))
    sum_y2 = sum((y ** 2 for y in rating2))
    denominator_x = sqrt(sum_x2 - ((sum_x ** 2) / n))
    denominator_y = sqrt(sum_y2 - ((sum_y ** 2) / n))
    denominator = denominator_x * denominator_y
    return numerator / denominator


def main():
    print(users)
    print(pearson(users['Angelica'], users['Bill']))

if __name__ == '__main__':
    main()
