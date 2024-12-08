def sum_of_square_of_evens(numbers):
    # Recursive function to sum the square of even numbers
    def recursive_sum(numbers):
        if not numbers: # base case:if the list is empty
            return 0
        else:
            # Get the first number
            first, *rest = numbers
            # check if the first number is even and calculate its square if it is
            square = first**2 if first % 2 == 0 else 0
            # Recursively call the function on the rest of the numbers
            return square + recursive_sum(rest)
        
    # using filter and map to create a list of square of even numbers
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared_evens = map(lambda x: x**2, even_numbers)
        
    # Return the sum using the recursive function
    return recursive_sum(list(squared_evens))

# Example usage
numbers = [1,2,3.4,5,6,7,8,9,10]
result = sum_of_square_of_evens(numbers)
print(f"The sum of the square of even numbers is: {result}")
