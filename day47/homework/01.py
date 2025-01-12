def check_number():
    try:
        number = float(input("შეიყვანეთ რიცხვი: "))
        
        if number > 0:
            print("შეყვანილი რიცხვი არის დადებითი.")
        elif number < 0:
            print("შეყვანილი რიცხვი არის უარყოფითი.")
        else:
            print("შეყვანილი რიცხვი არის ნულოვანი.")
    
    except ValueError:
        print("გთხოვთ, შეიყვანოთ ვალიდური რიცხვი.")


check_number()
