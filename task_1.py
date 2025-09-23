def find_max(numbers):
    if len(numbers) <= 1:
        return numbers[0]

    middle = len(numbers) // 2

    left_part = numbers[:middle]
    right_part = numbers[middle:]

    l = find_max(left_part)
    r = find_max(right_part)

    return l if l > r else r


print(find_max([10, 255, -3, 42, -5, 6, 79, 80]))
