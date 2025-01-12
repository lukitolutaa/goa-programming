def find_best_student():
    students = {}  
    best_student = None
    best_average = 0
    
    while True:
        name = input("შეიყვანეთ სტუდენტის სახელი (ან 'წასვლა' რომ დასრულდეს): ")
        
        if name.lower() == 'წასვლა': 
            break
        
        grades = input(f"შეიყვანეთ {name}-ის ნიშნები გამოყოფილი გხვედრით (მაგ: 8 9 10): ")
        
        grades = list(map(int, grades.split()))
        

        average = sum(grades) / len(grades)
        
        students[name] = average
        
        if average > best_average:
            best_average = average
            best_student = name
    
    if best_student:
        print(f"საუკეთესო სტუდენტი არის {best_student} საშუალო ნიშანით {best_average:.2f}")
    else:
        print("ვერ შევძელით საუკეთესო სტუდენტის გამოჩენა, რადგან არ არსებობს სტუდენტები.")

find_best_student()
