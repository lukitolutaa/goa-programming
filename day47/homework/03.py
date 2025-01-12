def separate_even_odd(numbers):
    even_numbers = []  
    odd_numbers = []   

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)  
        else:
            odd_numbers.append(num)  

    return even_numbers, odd_numbers  

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = separate_even_odd(numbers_list)

print("ლუწი რიცხვები:", even)
print("კენტი რიცხვები:", odd)
