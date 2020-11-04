def function_max(first_number, second_number, third_number):
    list_numbers = [first_number, second_number, third_number]
    list_numbers.remove(min(first_number, second_number, third_number))
    return sum(list_numbers)


print(function_max(4, 5, 7))
