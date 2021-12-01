# generate fibonnaci sequence
def generate_fibonnaci_sequence():
    fibonnaci_sequence = [1, 2]
    while fibonnaci_sequence[-1] < 4000000:
        fibonnaci_sequence.append(fibonnaci_sequence[-1] + fibonnaci_sequence[-2])

    del fibonnaci_sequence[-1]
    return fibonnaci_sequence


# get even numbers in fibonnaci sequence
def even_fibonnaci_numbers():
    fib_sequence = generate_fibonnaci_sequence()
    even_fibonnaci = []

    for number in fib_sequence:
        if number % 2 == 0:
            even_fibonnaci.append(number)

    return even_fibonnaci


# sum of even numbers
def sum_even_numbers():
    even_numbers = even_fibonnaci_numbers()
    counter = 0

    for number in even_numbers:
        counter += number

    return counter


print(generate_fibonnaci_sequence())
print(even_fibonnaci_numbers())
print(sum_even_numbers())
