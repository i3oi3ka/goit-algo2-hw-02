def find_max_min(numbers):
    """
    Find the maximum and minimum elements in a list using the
    divide and conquer approach.

    This function recursively splits the input list into halves,
    computes the maximum and minimum for each half, and then combines
    the results to determine the overall maximum and minimum.

    Parameters
    ----------
    numbers : list of int or float
        The list of numbers to search.

    Returns
    -------
    tuple
        A tuple (max_value, min_value) where:
        - max_value is the largest number in the list
        - min_value is the smallest number in the list

    Examples
    --------
    >>> find_max_min([10, 255, -3, 42, 5, 6, 7, 8])
    (255, -3)
    """
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    if len(numbers) == 2:
        return (max(numbers), min(numbers))

    middle = len(numbers) // 2

    left_part = numbers[:middle]
    right_part = numbers[middle:]

    l_max, l_min = find_max_min(left_part)
    r_max, r_min = find_max_min(right_part)

    return (l_max if l_max > r_max else r_max, l_min if l_min < r_min else r_min)


print(find_max_min([10, 255, -3, 42, 5, 6, 7, 8]))
