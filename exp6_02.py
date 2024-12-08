def sum_of_square_of_evens(numbers):
    def recursive_sum(squared_evens):
        if not squared_evens:
            return 0
        else:
            first,*rest = squared_evens
            return first + recursive_sum(rest)
    even_numbers = filter(lambda x: x%2 == 0,numbers)
    squared_evens = map(lambda x: x**2 , even_numbers)
    return recursive_sum(list(squared_evens))

numbers=[1,2,3,4,5,6,7,8,9,10]
result = sum_of_square_of_evens(numbers)
print(f"the sum of the square of even number is :{result}")
