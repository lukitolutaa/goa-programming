def filter_grades():
    grades_input = input("შეიყვანეთ სტუდენტების ქულები გამოყოფილი სივრცით (მაგ: 45 55 60 50): ")

    grades = list(map(int, grades_input.split()))

    filtered_grades = [grade for grade in grades if grade > 50]

    print(f"სტუდენტები, ვისაც აქვთ 50-ზე მეტი ქულა: {filtered_grades}")

filter_grades()
