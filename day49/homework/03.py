def reverse_numbers():

    numbers = input("შეიყვანეთ რიცხვები (ცალ-ცალკე ციფრები გამოყავით space-ით): ")
    
    numbers_list = numbers.split()

    reversed_list = numbers_list[::-1]

    print("შებრუნებული რიცხვები:", " ".join(reversed_list))

reverse_numbers()
