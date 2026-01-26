import sys
import itertools

#create learge dummy file
with open('large_file.csv' , 'w') as f:
    for i in range(1000000):
        f.write(f"{i},data_{i}\n")

# memory heave approach
lines_list = [line.strip().upper for line in open('large_file.csv')]
print(f"List comprehension memory usage: {sys.getsizeof(lines_list)} bytes")