# #  Python program to remove duplicates & print sum of numbers in a list

# # Function test

my_list = [5, 5, 2, 2, 6, 7,8]

def remove_duplicates_and_print_sum(my_list):
    unique_numbers = list(set(my_list))
    total_sum = sum(unique_numbers)
    print("Original list: ", my_list)
    print("Unique list: ", unique_numbers)

    return total_sum 




result = remove_duplicates_and_print_sum(my_list)

print("Sum of unique elements: ", result)
