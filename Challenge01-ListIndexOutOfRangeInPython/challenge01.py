#there is a bug here
#and we bet you can't find it
#share your answers in the comments

numbers = [1, 2, 3, 4, 5]
total = 0

for i in range(len(numbers)):
    total += numbers[i + 1]
    #IndexError: list index out of range
print(total)

