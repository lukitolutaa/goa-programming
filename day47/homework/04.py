def calculate_average(numbers):
    if len(numbers) == 0:  
        return "სიამ არაკორექტული მონაცემები: ცარიელი სია"
    
    total = sum(numbers)  
    count = len(numbers)  
    
    average = total / count  
    return average


numbers_list = [1, 2, 3, 4, 5]
average = calculate_average(numbers_list)
print("საშუალო რიცხვი:", average)

