import functions

result1 = functions.sum_and_sorted(15, 8)
print(result1)

result2 = functions.sum_and_sorted_verbose(20, verbose=True)
print(result2)

import functions

help(functions)
help(functions.sum_and_sorted)
help(functions.sum_and_sorted_verbose)



#Results from directory:
#ryankavanaugh@Ryans-MacBook-Pro Assignment 10 % python3 functions.py
#(23, [8, 15])
#Parameters:
#num1: 20
#num2: 3.141592653589793
#verbose: True
#Results:
#Sum: 23.141592653589793
#Sorted List: [3.141592653589793, 20]
#(23.141592653589793, [3.141592653589793, 20])
