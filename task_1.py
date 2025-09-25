def find_max_min(numbers):
    if len(numbers) <= 1:
        return numbers[0], numbers[0]

    middle = len(numbers) // 2

    left_part = numbers[:middle]
    right_part = numbers[middle:]

    l_max, l_min = find_max_min(left_part)
    r_max, r_min = find_max_min(right_part)

    return (l_max if l_max > r_max else r_max, l_min if l_min < r_min else r_min)


print(find_max_min([10, 255, -3, 42, 5, 6, 7, 8]))
