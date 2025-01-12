def process_grades():
    grades_input = input("შეიყვანეთ სტუდენტების ქულები გამოყოფილი სივრცით (მაგ: 7 8 9 10): ")

    grades = list(map(int, grades_input.split()))
    
    if len(grades) == 0:
        print("ქულები არ არის შეყვანილი!")
        return

    max_grade = max(grades)
    min_grade = min(grades)
    average_grade = sum(grades) / len(grades)

    print(f"მაქსიმალური ქულა: {max_grade}")
    print(f"მინიმალური ქულა: {min_grade}")
    print(f"საშუალო ქულა: {average_grade:.2f}")

process_grades()
