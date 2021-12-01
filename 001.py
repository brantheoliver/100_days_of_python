def it_sum_divisible_by(number: int) -> int:
    counter = 0
    for i in range(1000):
        if i % number == 0:
            counter += i
    return counter


def calc_sum_divisible_by(number: int) -> int:
    target = 999
    p = target // number

    return number * (p * (p + 1)) // 2


print(it_sum_divisible_by(3) + it_sum_divisible_by(5) - it_sum_divisible_by(15))
print(calc_sum_divisible_by(3) + calc_sum_divisible_by(5) - calc_sum_divisible_by(15))
