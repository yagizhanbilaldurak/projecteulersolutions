# palindrome number
numbers_list= []           # i created this list for saving all the numbers which equals i*j
palindrome_numbers_list = []  # i created this list for saving palindrome numbers
for j in range(100,1000):
    for i in range(100,1000):
        number = i*j
        numbers_list.append(number)
for element in numbers_list:
    element = str(element)  # converted integers into string because of reverse operation.
    if element == element[::-1]:
        element = int(element)  # converted into integers back in that way i can determine largest one.
        palindrome_numbers_list.append(element)
largest_palindrome = max(palindrome_numbers_list)
print(largest_palindrome)