def average_of_list(num_list):
    if len(num_list) == 0:
        return 0 
    total = 0  
    for num in num_list:
        total += num  
    average = total / len(num_list)  
    return average  

numbers = [1, 2, 3, 4, 5]
result = average_of_list(numbers)

print(f"რიცხვების საშუალო მნიშვნელობა არის: {result}")
