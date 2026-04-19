numbers = [9, 5, 8, 7, 4, 6, 1]

print("LIST RETURN METHOD #1")
print(numbers[1:6:2])     # full slice syntax - start:stop:step

print("LIST RETURN METHOD #2 (start)")
print(numbers[3])      # NOT SLICE METHOD - starts at index 3

print("LIST RETURN METHOD #3 (stop)")
print(numbers[:3])      # prints till index 2

print("LIST RETURN METHOD #3 (step)")
print(numbers[::2])     # prints index with 2 steps (index 1, 3, 5, 7...)

print("LIST RETURN METHOD #4 (reverse)")
print(numbers[::-1])     # prints reverse

print("LIST RETURN METHOD #5 (no brackets and commas)")
print(*numbers)         # this prints all items in the list (w/o brackets by using '*')

print("LIST RETURN METHOD #5.1 (brackets)")
print(numbers)          # with brackets