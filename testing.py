my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_odd = float('-inf')

for num in my_list:
    if num % 2 != 0 and num > max_odd:
        max_odd = num

if max_odd != float('-inf'):
    print("The maximum odd integer in the list is:", max_odd)
else:
    print("There are no odd integers in the list.")