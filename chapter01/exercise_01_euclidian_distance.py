from math import sqrt


def euclidian_distance(row1, row2):
    '''
        >>> angelica = (3.5, 2, None, 4.5, 5, 1.5, 2.5, 2)
        >>> bill = (2, 3.5, 4, None, 2, 3.5, None, 3)
        >>> euclidian_distance(angelica, bill)
        4.3
    '''

    factors = 0
    for r1, r2 in zip(row1, row2):
        if r1 is not None and r2 is not None:
            factors += (r1 - r2) ** 2
    return sqrt(factors)


def main():
    bands = ('Blues Traveler', 'Broken Bells', 'Deadmau5', 'Norah Jones',
             'Phoenix', 'Slightly Stoopid', 'The Strokes', 'Vampire Weekend')
    angelica = (3.5, 2, None, 4.5, 5, 1.5, 2.5, 2)
    bill = (2, 3.5, 4, None, 2, 3.5, None, 3)
    # chan = (5, 1, 1, 3, 5, 1, None, None)
    # dan = (3, 4, 4.5, None, 3, 4.5, 4, 2)
    hailey = (None, 4, 1, 4, None, None, 4, 1)
    jordyn = (None, 4.5, 4, 5, 5, 4.5, 4, 4)
    # sam = (5, 2, None, 3, 5, 4, 5, None)
    veronica = (3, None, None, 5, 4, 2.5, 3, None)
    print(bands)
    print(euclidian_distance(angelica, bill))
    print(euclidian_distance(hailey, veronica))
    print(euclidian_distance(hailey, jordyn))


if __name__ == '__main__':
    main()
