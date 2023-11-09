import math

def sum_and_sorted(num1, num2=math.pi):
    """
    Calculate the sum of two numbers and return them as well as a sorted list.

    Args:
        num1 (float): The first number.
        num2 (float): The second number (default is math.pi).

    Returns:
        tuple: A tuple containing the total sum and a sorted list of the two numbers.
    """
    num_list = [num1, num2]
    sorted_list = sorted(num_list)
    total_sum = num1 + num2
    return total_sum, sorted_list

def sum_and_sorted_verbose(num1, num2=math.pi, verbose=False):
    """
    Calculate the sum of two numbers and return them as well as a sorted list. If verbose is True, print the parameters and results.

    Args:
        num1 (float): The first number.
        num2 (float): The second number (default is math.pi).
        verbose (bool): If True, print parameters and results.

    Returns:
        tuple: A tuple containing the total sum and a sorted list of the two numbers.
    """
    num_list = [num1, num2]
    sorted_list = sorted(num_list)
    total_sum = num1 + num2
    if verbose:
        print("Parameters:")
        print(f"num1: {num1}")
        print(f"num2: {num2}")
        print(f"verbose: {verbose}")
        print("Results:")
        print(f"Sum: {total_sum}")
        print(f"Sorted List: {sorted_list}")
    return total_sum, sorted_list



if __name__ == "__main__":
    result1 = sum_and_sorted(15, 8)
    print(result1)

    result2 = sum_and_sorted_verbose(20, verbose=True)
    print(result2)
