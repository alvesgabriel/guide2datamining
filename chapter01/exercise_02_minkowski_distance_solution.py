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


def manhattan(rating1, rating2):
    '''Computes the Manhattan distance. Both rating1 and rating2 are
    dictionaries of the form 'Slightly Stoopid': 2.5 ...

    >>> from exercise_01_euclidian_distance_solution import users
    >>> manhattan(users['Hailey'], users['Veronica'])
    2.0
    '''
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance


def minkowski(r, rating1, rating2):
    '''Computes the Minkowski distance.
    Both rating1 and rating2 are dictionaries of the form
    {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}'''
    distance = 0
    common_ratings = False
    for key in rating1:
        if key in rating2:
            distance += pow(abs(rating1[key] - rating2[key]), r)
            common_ratings = True
    if common_ratings:
        return pow(distance, (1 / r))
    return 0


def compute_neares_neighbor(username, users):
    '''creates a sorted list of users based on their distance to
    username

    >>> from exercise_01_euclidian_distance_solution import users
    >>> compute_neares_neighbor("Hailey", users)
    [(2.0, 'Veronica'), (4.0, 'Chan'), (4.0, 'Sam'), (4.5, 'Dan'), (5.0, 'Angelica'), (5.5, 'Bill'), (7.5, 'Jordyn')]
    >>> compute_neares_neighbor('Angelica', users)
    [(3.5, 'Veronica'), (4.5, 'Chan'), (5.0, 'Hailey'), (8.0, 'Sam'), (9.0, 'Bill'), (9.0, 'Dan'), (9.5, 'Jordyn')]
    '''
    distances = []
    for user in users:
        if user != username:
            distance = minkowski(1, users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances


def recommend(username, users):
    '''Give list of recommendations

    >>> from exercise_01_euclidian_distance_solution import users
    >>> recommend('Hailey', users)
    [('Phoenix', 4.0), ('Blues Traveler', 3.0), ('Slightly Stoopid', 2.5)]
    >>> recommend('Chan', users)
    [('The Strokes', 4.0), ('Vampire Weekend', 1.0)]
    >>> recommend('Sam', users)
    [('Deadmau5', 1.0)]
    >>> recommend('Angelica', users)
    []
    '''
    # first find nearests neighbor
    nearest = compute_neares_neighbor(username, users)[0][1]
    recommendations = []
    # now find bands neighbor rated that user didn't
    neighbor_ratings = users[nearest]
    user_rating = users[username]
    for artist in neighbor_ratings:
        if artist not in user_rating:
            recommendations.append((artist, neighbor_ratings[artist]))
    # using the function sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artist_tuple: artist_tuple[1], reverse=True)


def main():
    print(users)
    recommend('Hailey', users)


if __name__ == '__main__':
    main()
