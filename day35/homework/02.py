numbers = list(range(1, 11))

first_half = numbers[:5]

second_half = numbers[5:]

squares = [x ** 2 for x in numbers]

print("First half:", first_half)
print("Second half:", second_half)
print("Squares:", squares)