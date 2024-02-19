#Задача 1
def merge_and_sort_arrays(*arrays):

    merged_array = [item for sublist in arrays for item in sublist]

    no_multiples_of_five = [num for num in merged_array if num % 5 != 0]

    unique_numbers = list(set(no_multiples_of_five))

    sorted_array = sorted(unique_numbers)

    return sorted_array

print(merge_and_sort_arrays([1, 2, 3, 10223], [7, 10, 9, 20], [10, 17, 30, 62]))
