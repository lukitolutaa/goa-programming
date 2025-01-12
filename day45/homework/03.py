def reverse_list(items):
    reversed_items = []  
    for item in items:  
        reversed_items.insert(0, item) 
    return reversed_items  


original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)

print(f"წინაპარი სია: {original_list}")
print(f"გადაბრუნებული სია: {reversed_list}")
