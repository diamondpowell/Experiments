#find squares of all even numbers under 1 mil, but only keep the results less than 1k

# 1. start with a sequence of numbers
numbers = range(1, 1000000) # range from 0-1mil

#2. chain a generator to filter for even numbers
evens = (x for x in numbers if x % 2 == 0)  # all numbers if they are even

# 3. chain another generator to square them
squares = (x**2 for x in evens)

# 4. chain a final generator to filter the results
filtered = (x for x in squares if x < 1000) #check if all squares are less than 1k

# the data is only processed when we iterate over 'filtered'
print(list(filtered))  # Output the final results