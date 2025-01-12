def calculator(num1, num2, operation):
    if operation == "დამატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
        return num1 / num2
    else:
        return "შეცდომა: არა სწორი ოპერაცია"


print(calculator(10, 5, "დამატება"))     
print(calculator(10, 5, "გამოკლება"))    
print(calculator(10, 5, "გამრავლება"))    
print(calculator(10, 5, "გაყოფა"))       
print(calculator(10, 0, "გაყოფა"))       
print(calculator(10, 5, "არასწორი"))