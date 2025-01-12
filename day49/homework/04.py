def calculate_average():
  
    numbers = input("შეიყვანეთ რიცხვები (ცალ-ცალკე ციფრები space-ით): ")

    numbers_list = numbers.split()
    
    numbers_list = [float(num) for num in numbers_list]  

    if len(numbers_list) == 0:
        print("რიცხვების რაოდენობა არ არის შესული.")
    else:
        average = sum(numbers_list) / len(numbers_list)

        print(f"შედეგი: რიცხვების საშუალო მნიშვნელობა არის: {average}")

calculate_average()
