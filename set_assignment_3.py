# Python program to remove duplicate amounts & print sum of amounts minus 7% vat


my_amount = [29.50, 25.00, 25.00, 50.00, 60.00, 40.00, 40.00, 5.50]

def remove_duplicates_and_print_sum_vat(my_amount):
    unique_amount = list(set(my_amount))
    sum_total = sum(unique_amount)
    vat = int(sum_total * 0.07)
    grand_total = sum_total - vat
    print("Original list: ", my_amount)
    print("Unique list: ", unique_amount)
    print("Total sum is: ", sum_total)
    print("VAT is: ", vat)

    return grand_total 


result = remove_duplicates_and_print_sum_vat(my_amount)

print("Sum of amounts after vat: ",result)