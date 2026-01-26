import sys
import itertools

#create learge dummy file
with open('large_file.csv' , 'w') as f:
    for i in range(1000000):
        f.write(f"{i},data_{i}\n")